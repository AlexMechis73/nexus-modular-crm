# Nexus CRM – Modular CRM per PMI e Team

Sistema CRM modulare, flessibile e self-hosted, sviluppato per l’ottimizzazione delle attività di marketing, vendite e customer experience.

## 📦 Struttura del progetto

- `src/`: codice backend e frontend (moduli e app)
- `db/`: schema e script SQL
- `docker/`: ambienti di deploy containerizzati
- `docs/`: documentazione tecnica e funzionale
- `monitoring/`: strumenti per health check e logging

## 🚀 Tecnologie principali

- Python / FastAPI
- PostgreSQL
- Supabase
- Streamlit
- Docker / Docker Compose

## 🔐 Requisiti minimi

- Docker e Docker Compose installati
- Python 3.10+
- Git

## 🛠️ Setup rapido

```bash
git clone https://github.com/AlexMechis73/nexus-modular-crm.git
cd nexus-modular-crm
docker-compose up --build
