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

---

### FASE 1: MVP CORE - CRM PER IL COMMERCIALE (In Corso)

**Obiettivo:** Sviluppare le funzionalità base di gestione Contatti e Lead, proteggendole con l'autenticazione.
**Stima Tempo:** 5-7 giorni lavorativi.

| Task ID | Task                                       | Deliverable                                         | Stato      |
| :------ | :----------------------------------------- | :-------------------------------------------------- | :--------- |
| **1.1** | **Implementare Protezione Endpoint** | Creare un endpoint protetto `/users/me` che restituisce i dati dell'utente loggato. | Endpoint accessibile solo con token JWT valido.     | ✅ **Fatto** |
| **1.2** | **Definire Schema Contatti/Lead** | Aggiungere i modelli `Contact` e `Lead` al file `schema.prisma`. | Schema aggiornato.                                  | ⬜ **Prossimo Task** |
| **1.3** | **Migrare Nuovo Schema DB** | Eseguire `prisma migrate dev` per aggiungere le nuove tabelle. | Tabelle `Contact` e `Lead` create nel DB.          | ⬜ Da fare  |
| **1.4** | **Sviluppare CRUD API per Contatti** | Creare gli endpoint API (`GET`, `POST`, `PUT`) per i contatti. | API per la gestione dei contatti.                   | ⬜ Da fare  |
| **1.5** | **Integrare Permessi nel CRUD** | Assicurarsi che ogni endpoint verifichi che l'utente possa agire solo sui propri dati. | Logica dei permessi implementata e sicura.          | ⬜ Da fare  |

---

### FASE 2: ANALYTICS & DASHBOARD (MVP)

**Obiettivo:** Fornire una dashboard con i KPI fondamentali per un agente e per il management.
**Stima Tempo:** 4-6 giorni lavorativi.

| Task ID | Task                                       | Deliverable                                         | Stato      |
| :------ | :----------------------------------------- | :-------------------------------------------------- | :--------- |
| **2.1** | **Progettazione KPI con Stakeholder** | Definire 2-3 KPI chiave da visualizzare (es. Nuovi Lead/mese, Tasso Conversione). | Specifiche funzionali per i KPI.                    | ⬜ Da fare  |
| **2.2** | **Sviluppo Script ETL/Analytics** | Creare o adattare script Python che calcolano i KPI e li salvano in tabelle di riepilogo. | Script eseguibili.                                | ⬜ Da fare  |
| **2.3** | **Definire Schema Dati Analytics** | Aggiungere modelli `AnalyticsSummary` al `schema.prisma`. | Schema aggiornato.                                  | ⬜ Da fare  |
| **2.4** | **Creare Endpoint API per Dashboard** | Sviluppare un endpoint protetto `GET /dashboard/summary` che recupera i dati aggregati. | API che espone i dati per la dashboard.             | ⬜ Da fare  |
| **2.5** | **Sviluppare Componente UI Dashboard** | Creare un primo componente SvelteKit che visualizza i KPI. | Dashboard base nell'interfaccia utente.              | ⬜ Da fare  |

---

### FASE 3: INTEGRAZIONE MODULO PERCORSI

**Obiettivo:** Integrare il microservizio esistente per l'ottimizzazione dei percorsi di visita.
**Stima Tempo:** 3-5 giorni lavorativi.

| Task ID | Task                                       | Deliverable                                         | Stato      |
| :------ | :----------------------------------------- | :-------------------------------------------------- | :--------- |
| **3.1** | **Analisi Microservizio Esistente** | Analizzare l'API, l'input e l'output del servizio di routing esistente. | Documento di analisi tecnica.                       | ⬜ Da fare  |
| **3.2** | **Definire Contratto API Integrazione** | Progettare come il CRM Core Service comunicherà con il servizio di routing. | Specifiche API per l'integrazione.                  | ⬜ Da fare  |
| **3.3** | **Sviluppare Livello di Integrazione** | Scrivere il codice nel CRM Core Service per chiamare l'API del routing. | Codice di integrazione funzionante.                 | ⬜ Da fare  |
| **3.4** | **Aggiungere Funzionalità UI** | Aggiungere un pulsante "Ottimizza Percorso" nell'interfaccia dei clienti/visite. | Pulsante e interazione UI.                          | ⬜ Da fare  |
| **3.5** | **Test End-to-End** | Verificare che il flusso completo (dal click al risultato della rotta) funzioni. | Test case superato.                                 | ⬜ Da fare  |