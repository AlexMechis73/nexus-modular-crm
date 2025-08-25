# services/crm-core-service/main.py

from prisma.models import User, Contact
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from prisma import Prisma
from prisma.models import User

# --- Configurazione ---
app = FastAPI(title="Nexus CRM Core API")
# --- Configurazione Sicurezza (JWT) ---
SECRET_KEY = "la-tua-chiave-segreta-super-difficile" # In produzione, questa deve essere più complessa!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
prisma = Prisma(auto_register=True)

# Contesto per l'hashing delle password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Modelli di Dati (Pydantic) ---
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str
    email: EmailStr


class ContactBase(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    phone: str | None = None
    company: str | None = None
    role: str | None = None

class ContactCreate(ContactBase):
    pass

class ContactOut(ContactBase):
    id: str
    ownerId: str

# --- Funzioni di Utilità ---
def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Funzione di sicurezza """"Prende il token dalla richiesta, lo decodifica, e ci restituisce l'utente corrispondente dal database"""""
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    """
    Decodifica il token JWT, valida l'utente e lo restituisce.
    Lancia un'eccezione se il token non è valido o l'utente non esiste.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = await User.prisma().find_unique(where={"email": email})
    if user is None:
        raise credentials_exception
    return user

# --- Eventi di avvio e spegnimento dell'app ---
@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

# --- Endpoint API ---

# Funzione register_user che gestisce la registrazione di un nuovo utente
@app.post("/auth/register", status_code=status.HTTP_201_CREATED, response_model=UserOut, tags=["Authentication"])
async def register_user(user_data: UserCreate):
    """
    Registra un nuovo utente nel sistema.
    - Controlla se l'email esiste già.
    - Fa l'hash della password.
    - Salva il nuovo utente nel database.
    """
    existing_user = await User.prisma().find_unique(where={"email": user_data.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Un utente con questa email esiste già.",
        )

    hashed_password = hash_password(user_data.password)

    new_user = await User.prisma().create(
        data={
            "email": user_data.email,
            "password": hashed_password,
        }
    )
    return new_user

# Funzione read_root che restituisce lo stato del servizio
@app.get("/", tags=["Status"])
def read_root():
    return {"status": "Nexus CRM Core Service is running"}

# Funzione login_for_access_token che gestisce il login e restituisce un token JWT
@app.post("/auth/login", tags=["Authentication"])
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await User.prisma().find_unique(where={"email": form_data.username})
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o password non corretti",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# Funzione read_users_me che restituisce i dati dell'utente attualmente autenticato
@app.get("/users/me", response_model=UserOut, tags=["Users"])
async def read_users_me(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Restituisce i dati dell'utente attualmente autenticato.
    Questo endpoint è protetto: richiede un token JWT valido.
    """
    # Per ora, non validiamo il token, ma la dipendenza Depends(oauth2_scheme)
    # già blocca le richieste che non hanno un token.
    # Nelle prossime fasi, decodificheremo il token per ottenere l'email dell'utente.

    # Per questo test, cerchiamo un utente fittizio per restituire qualcosa.
    # In futuro, l'email verrà estratta dal token.
    user = await User.prisma().find_unique(where={"email": "test-login@example.com"}) # Usa un'email che hai registrato
    if user is None:
        raise HTTPException(status_code=404, detail="Utente non trovato per il test")

    return user


@app.get("/users/me", response_model=UserOut, tags=["Users"])
async def read_users_me(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Restituisce i dati dell'utente attualmente autenticato.
    Questo endpoint è protetto: richiede un token JWT valido per accedervi.
    """
    # Nelle prossime fasi, qui decodificheremo il token per ottenere
    # l'email dell'utente e recuperare i suoi dati specifici.

    # Per questo primo test, restituiamo un utente fittizio per confermare
    # che la protezione funziona. Assicurati di aver registrato questo utente.
    user = await User.prisma().find_unique(where={"email": "primo.utente@mac.com"}) 
    if user is None:
        raise HTTPException(status_code=404, detail="Utente di test non trovato. Registralo prima.")

    return user


# --- API CRUD per i Contatti ---

# Funzione create_contact che crea un nuovo contatto per l'utente autenticato
@app.post("/contacts", response_model=ContactOut, tags=["Contacts"], status_code=status.HTTP_201_CREATED)
async def create_contact(
    contact_data: ContactCreate, 
    current_user: Annotated[User, Depends(get_current_user)]
):
    """
    Crea un nuovo contatto per l'utente attualmente autenticato.
    """
    new_contact = await Contact.prisma().create(
        data={
            **contact_data.dict(),
            "ownerId": current_user.id, # <-- USA L'ID DELL'UTENTE REALE
        }
    )
    return new_contact

# Funzione get_all_contacts che restituisce i contatti dell'utente autenticato 
@app.get("/contacts", response_model=list[ContactOut], tags=["Contacts"])
async def get_all_contacts(
    current_user: Annotated[User, Depends(get_current_user)]
):
    """
    Restituisce un elenco dei contatti che appartengono SOLO all'utente autenticato.
    """
    contacts = await Contact.prisma().find_many(
        where={"ownerId": current_user.id} # <-- FILTRA I CONTATTI PER L'UTENTE
    )
    return contacts

