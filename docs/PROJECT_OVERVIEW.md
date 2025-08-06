# Panoramica del Progetto NEXUS-CRM

## 1. Introduzione e Obiettivi

NEXUS-CRM è un sistema di Customer Relationship Management (CRM) modulare, sicuro e performante, progettato su misura per le esigenze del team commerciale di **TSvapo**. L'obiettivo primario del progetto è fornire uno strumento open-source, veloce e a basso costo operativo per ottimizzare la gestione di clienti, prospect, pianificazione delle visite e analisi delle vendite.

La filosofia alla base del progetto è la **modularità**, che permette di sviluppare, integrare e mantenere le funzionalità in modo indipendente, garantendo la scalabilità futura del sistema.

## 2. Architettura dei Moduli

Il sistema è scomposto in moduli funzionali interconnessi, ognuno con un obiettivo specifico.

### Modulo 0: Autenticazione & Sicurezza (Core)
* **Stato:** ✅ **Completato**
* **Descrizione:** Costituisce le fondamenta sicure dell'intera applicazione. Gestisce la registrazione di nuovi utenti, il processo di login tramite token JWT (JSON Web Tokens) e la protezione degli endpoint API. È la base per il futuro sistema di permessi a più livelli (RBAC).

### Modulo 1: CRM Core (Clienti, Lead & Trattative)
* **Stato:** ⬜ **In Sviluppo**
* **Descrizione:** È il cuore funzionale del CRM. Questo modulo gestirà l'anagrafica completa di clienti e prospect (`clients`). Implementerà inoltre la logica per la gestione del funnel di vendita, tracciando le opportunità commerciali (`opportunity`) e il loro avanzamento attraverso la pipeline di vendita (`sales_pipeline`). Tutte le operazioni saranno protette e attribuite all'utente che le esegue.

### Modulo 2: Visite & Percorsi
* **Stato:** ⬜ **Pianificato**
* **Descrizione:** Questo modulo si occuperà della pianificazione e dello scheduling delle attività e delle visite presso i clienti (`visits`). Prevede l'integrazione con il microservizio esistente per l'ottimizzazione geografica dei percorsi, fornendo agli agenti lo strumento per pianificare i loro giri in modo efficiente.

### Modulo 3: Analytics & Dashboard
* **Stato:** ⬜ **Pianificato**
* **Descrizione:** L'obiettivo di questo modulo è trasformare i dati grezzi in insight strategici. Attraverso una dashboard, visualizzerà i KPI fondamentali per il business, come l'andamento delle vendite, lo stato dei lead e le metriche di conversione, basandosi sulla mappatura del Customer Journey.

### Modulo Futuro: Loyalty
* **Stato:** 🕓 **Pianificato (Lungo Termine)**
* **Descrizione:** In futuro, il sistema potrà essere esteso con un modulo dedicato alla gestione di programmi di fidelizzazione per i clienti.

## 3. Stack Tecnologico

Il progetto si basa su uno stack tecnologico moderno e interamente open-source per massimizzare l'efficienza e minimizzare i costi.
* **Backend:** Python con il framework **FastAPI**.
* **Database:** **PostgreSQL**, gestito tramite l'ORM **Prisma**.
* **Ambiente di Sviluppo e Produzione:** **Docker** e Docker Compose.
* **Frontend (Pianificato):** **SvelteKit**.