# services/crm-core-service/main.py

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from prisma import Prisma
from prisma.models import User

# --- Configurazione ---
app = FastAPI(title="Nexus CRM Core API")
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
