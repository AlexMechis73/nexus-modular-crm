# 🧱 FASE 2 – RISTRUTTURAZIONE ARCHITETTURALE HEXAGONALE (NEXUS-CRM-TSVAPO)

## 📅 Data completamento: 2025-07-26

---

## 🎯 Obiettivo
Ristrutturare il progetto secondo l’architettura esagonale (Hexagonal Architecture), anche detta Ports and Adapters, per garantire una maggiore scalabilità, testabilità e separazione delle responsabilità.

---

## ✅ Attività completate

1. **Creazione delle directory principali:**
   - `domain/` – entità di dominio, value object, aggregati
   - `application/` – casi d’uso e servizi di business
   - `infrastructure/` – adapter di persistenza, email, notifiche, database, ecc.
   - `interfaces/` – router FastAPI, viewmodel, API, CLI
   - `config/` – configurazioni di sistema, env, logger

2. **Spostamento dei router**
   - La cartella `routers/` è stata spostata in `interfaces/` per riflettere il ruolo come entrypoint API (adapter in input).

---

## 🧠 Prossimi step

- Rifattorizzare `main.py` per caricare i router da `interfaces/routers/`
- Definire i primi oggetti nel dominio (`domain/`)
- Creare un esempio di caso d’uso (`application/`) e collegarlo
- Definire le dipendenze tra le componenti mantenendo i livelli isolati

---

## 🧩 Commenti del CTO
> "Questa struttura ci consente di scalare il progetto in modo ordinato e testabile. La separazione esplicita tra logica di dominio e adapter semplifica anche l'integrazione futura di database, sistemi esterni e test automatizzati."

