# services/crm-core-service/main.py

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

# --- Eventi di avvio e spegnimento dell'app ---
@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()

# --- Endpoint API ---
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

@app.get("/", tags=["Status"])
def read_root():
    return {"status": "Nexus CRM Core Service is running"}

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