# src/Dockerfile.streamlit
FROM python:3.10.14-slim

# Update system and install security patches
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create and use a non-root user
RUN useradd -m appuser
USER appuser

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
