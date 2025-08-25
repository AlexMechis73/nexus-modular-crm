# services/crm-core-service/main.py
# VERSIONE AGGIORNATA CON LE NUOVE API PER I CONTATTI

from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr

# Importiamo TUTTI i nuovi modelli da Prisma
from prisma import Prisma
from prisma.models import Contact, Interaction, Lead, Order, Proposal, User, Visit
from prisma.errors import UniqueViolationError # Importiamo l'errore per gestirlo

# --- Configurazione ---
app = FastAPI(title="Nexus CRM Core API - v2")
prisma = Prisma(auto_register=True)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Configurazione Sicurezza (JWT) ---
SECRET_KEY = "la-tua-chiave-segreta-super-difficile"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# --- Eventi di avvio e spegnimento dell'app ---
@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    if prisma.is_connected():
        await prisma.disconnect()

# --- Modelli di Dati (Pydantic) ---

class UserOut(BaseModel):
    id: str
    email: EmailStr

# +++ NUOVI MODELLI PYDANTIC PER I CONTATTI +++
class ContactCreate(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    phone: str | None = None
    company: str | None = None

class ContactOut(BaseModel):
    id: str
    firstName: str
    lastName: str
    email: EmailStr
    phone: str | None = None
    company: str | None = None
    ownerId: str

# --- Funzioni di Utilità (Hashing e Token) ---
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

# --- Dipendenza di Sicurezza ---
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
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


# --- Endpoint API ---

@app.get("/", tags=["Status"])
def read_root():
    return {"status": "Nexus CRM Core Service v2 is running"}

# --- Autenticazione ---

class UserCreate(BaseModel):
    email: EmailStr
    password: str

@app.post("/auth/register", status_code=status.HTTP_201_CREATED, response_model=UserOut, tags=["Authentication"])
async def register_user(user_data: UserCreate):
    existing_user = await User.prisma().find_unique(where={"email": user_data.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Un utente con questa email esiste già.",
        )

    hashed_password = hash_password(user_data.password)
    new_user = await User.prisma().create(
        data={"email": user_data.email, "password": hashed_password}
    )
    return new_user

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
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    """Restituisce i dati dell'utente attualmente autenticato."""
    return current_user

# +++ NUOVE API RICOSTRUITE PER I CONTATTI +++

@app.post(
    "/contacts",
    response_model=ContactOut,
    tags=["Contacts"],
    status_code=status.HTTP_201_CREATED,
)
async def create_contact(
    contact_data: ContactCreate,
    current_user: Annotated[User, Depends(get_current_user)],
):
    """
    Crea un nuovo contatto per l'utente autenticato.
    Gestisce l'errore nel caso in cui l'email del contatto esista già.
    """
    try:
        new_contact = await Contact.prisma().create(
            data={
                "firstName": contact_data.firstName,
                "lastName": contact_data.lastName,
                "email": contact_data.email,
                "phone": contact_data.phone,
                "company": contact_data.company,
                "ownerId": current_user.id,
            }
        )
        return new_contact
    except UniqueViolationError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Un contatto con l'email '{contact_data.email}' esiste già.",
        )

@app.get("/contacts", response_model=list[ContactOut], tags=["Contacts"])
async def get_contacts_for_current_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    """
    Restituisce la lista dei contatti che appartengono all'utente autenticato.
    """
    contacts = await Contact.prisma().find_many(where={"ownerId": current_user.id})
    return contacts