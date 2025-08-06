# Work Breakdown Structure (WBS) & Roadmap - NEXUS-CRM
*Ultimo aggiornamento: 6 agosto 2025*

Questo documento scompone le fasi di sviluppo, traccia lo stato di avanzamento e fornisce una stima di alto livello dei tempi.

---

### Stato Attuale Progetto
La configurazione dell'ambiente di sviluppo su macOS è stata completata con successo. L'ecosistema Docker (API + Database) è funzionante. Il modulo di autenticazione di base (Fase 0) è stato implementato e testato.

---

### FASE 0: FONDAMENTA - SICUREZZA E ACCESSO

**Obiettivo:** Creare un sistema di autenticazione e autorizzazione (RBAC) robusto.
**Stato:** ✅ **COMPLETATA**

| Task ID | Task                                    | Deliverable                                | Stato      |
| :------ | :-------------------------------------- | :----------------------------------------- | :--------- |
| **0.1** | **Setup Ambiente e DB** | Ambiente Docker funzionante con tabelle RBAC. | ✅ **Fatto** |
| **0.2** | **Creare Endpoint di Registrazione** | Endpoint `POST /auth/register` testabile.   | ✅ **Fatto** |
| **0.3** | **Implementare Hashing Password** | Funzione di hashing `passlib` integrata.    | ✅ **Fatto** |
| **0.4** | **Creare Endpoint di Login** | Endpoint `POST /auth/login` che genera token JWT. | ✅ **Fatto** |
| **0.5** | **Creare Middleware di Protezione** | Middleware per le rotte protette.          | ⬜ Da fare (Spostato a Fase 1) |

---

### FASE 1: MVP CORE - CRM PER IL COMMERCIALE (In Corso)

**Obiettivo:** Sviluppare le funzionalità base di gestione Contatti e Lead, proteggendole con l'autenticazione.
**Stima Tempo:** 5-7 giorni lavorativi.

| Task ID | Task                                       | Deliverable                                         | Stato      |
| :------ | :----------------------------------------- | :-------------------------------------------------- | :--------- |
| **1.1** | **Proteggere un Endpoint di Test** | Creare un endpoint `/users/me` che restituisce i dati dell'utente loggato. | Endpoint protetto da token JWT.                    | ⬜ **Prossimo Task** |
| **1.2** | **Definire Schema Contatti/Lead** | Aggiungere i modelli `Contact` e `Lead` al file `schema.prisma`. | Schema aggiornato.                                  | ⬜ Da fare  |
| **1.3** | **Migrare Nuovo Schema DB** | Eseguire `prisma migrate dev` per aggiungere le nuove tabelle. | Tabelle `Contact` e `Lead` create nel DB.          | ⬜ Da fare  |
| **1.4** | **Sviluppare CRUD API per Contatti** | Creare gli endpoint API (`GET`, `POST`, `PUT`) per i contatti. | API per la gestione dei contatti.                   | ⬜ Da fare  |
| **1.5** | **Integrare Permessi nel CRUD** | Assicurarsi che ogni endpoint verifichi che l'utente possa agire solo sui propri dati. | Logica dei permessi implementata e sicura.          | ⬜ Da fare  |

---

### Stime di Alto Livello (Roadmap / Simil-Gantt)

* **Fase 0: Autenticazione:** Completata il 6 Ago 2025.
* **Fase 1: CRM Core (Contatti/Lead):** Inizio 7 Ago - Stima Fine 15 Ago.
* **Fase 2: Analytics & Dashboard:** Stima 4-6 giorni lavorativi.
* **Fase 3: Integrazione Routing:** Stima 3-5 giorni lavorativi.