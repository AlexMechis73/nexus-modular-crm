FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- AGGIUNTA CHIAVE ---
# Copiamo lo schema PRIMA di copiare il resto del codice,
# così possiamo generare il client Prisma. Questo ottimizza anche la cache di Docker.
COPY ./prisma ./prisma/
RUN prisma generate
# --------------------

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]