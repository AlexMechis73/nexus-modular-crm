# 📜 Master Context Protocol (MCP)

## 🧠 Obiettivo del Documento
Fornire un protocollo di contesto completo e persistente per lo sviluppo del progetto **NEXUS-CRM per TSvapo**, ottimizzato per collaborazione tra me (Codex GPT-4o) e il referente tecnico del progetto, **Business Analyst & Data Scientist (BA&DS)**.

## 👤 Profilo Utente Tecnico
**Ruolo:** Business Analyst & Data Scientist  
**Competenze:**
- Esperienza nello sviluppo di **microservizi** (es. ottimizzazione visite, dashboard Streamlit)
- Esperienza con **Python**, **Streamlit**, **data cleaning**, **analisi statistica**
- Ha bisogno di **istruzioni chiare, guidate e operative** per lavorare su backend, architettura completa, CI/CD, testing e sviluppo modulare

## 📦 Progetto
**Nome:** NEXUS-CRM  
**Cliente:** TSvapo (azienda produttrice e distributrice di prodotti per vaping)  
**Obiettivo:** Creare un CRM modulare, sicuro, veloce, open-source per gestire clienti, prospect, pianificazioni e moduli futuri (es. loyalty, e-commerce)

## 🧱 Stack Tecnologico (baseline)
- **Frontend:** SvelteKit
- **Backend/API:** Node.js + Express
- **Database:** PostgreSQL + Prisma
- **Auth:** Supabase Auth con JWT + 2FA
- **Backup:** Scaleway S3 (crittografato)
- **CI/CD:** GitHub Actions (test + deploy)
- **Monitoring:** Netdata
- **Hosting:** Hetzner VPS (Ubuntu 22.04)

## 📂 Struttura Modulare
| Modulo        | Stato  | Descrizione                                 |
|---------------|--------|---------------------------------------------|
| Auth          | ✅     | Autenticazione e autorizzazione utenti      |
| Clienti       | ✅     | CRUD + filtri                               |
| Visite        | ✅     | Pianificazione, calendario                  |
| Dashboard     | 🔄     | KPI, andamento attività                     |
| Percorsi      | 🔄     | Ottimizzazione visite (Leaflet + OSRM)      |
| Loyalty       | 🕓     | Previsto Q2 2026                            |

## 📊 KPI Tecnici Monitorati
- Tempo medio risposta API < 500ms
- Caricamento UI < 1s
- Uptime 99.9%
- Costi operativi < €100/anno

## 🔐 Sicurezza
- JWT con refresh ogni 12h
- RBAC su ogni route + DB
- Crittografia AES-256
- Rate limiting su POST/PUT/DELETE
- Audit log modifiche
- Backup automatici giornalieri

## 📜 Guideline per Collaborazione (BA&DS ↔️ Codex)
- Ogni microservizio sviluppato da utente deve seguire una **struttura modulare dichiarata**
- Codex fornisce:
  - Specifiche tecniche in linguaggio chiaro
  - Esempi implementativi pronti all’uso
  - Script integrabili (SQL, Node.js, deploy)
  - Documentazione generata automaticamente
- BA&DS fornisce:
  - Logiche funzionali, KPI, input/output attesi
  - Test case e verifica validazione
  - Dataset, segmentazioni, esigenze di reporting

## 🛠️ Modalità di Esecuzione Guidata
1. Codex propone il **design del modulo** → Utente approva o modifica
2. Codex fornisce **codice pronto** + commenti tecnici + path d'inserimento nel progetto
3. Utente può:
   - Copiare e integrare
   - Richiedere modifiche
   - Verificare con propri dataset
4. Codex supporta nella **fase di test e deploy** con comandi guidati e documentazione

## 🔁 Sinergia prevista
> “Tu porti la logica, io il codice. Tu i dati, io la struttura. Tu le metriche, io il monitoraggio.”

## ✅ Prossimi step
1. Caricare repository GitHub con struttura base (es. `nexus-crm-tsvapo/`)
2. Inserire moduli già completati (auth, clienti, visite)
3. Attivare ambiente test su VPS Hetzner
4. Creare modulo **Dashboard** → KPIs giornalieri e visita prospect
5. Progettare modulo **Percorsi** integrato con dati geografici reali

---

> Documento persistente – ogni nuova funzione sarà connessa a questo contesto.

