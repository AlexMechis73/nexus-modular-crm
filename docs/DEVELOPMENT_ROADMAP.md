#### `DEVELOPMENT_ROADMAP.md`
```markdown
# Roadmap di Sviluppo NEXUS-CRM

## Principio Guida
Lo sviluppo è suddiviso in Fasi per rilasciare valore in modo iterativo e validare le funzionalità core prima di costruire l'intero ecosistema.

---

### **Fase 0: Fondamenta - Sicurezza e Accesso**
* **Obiettivo:** Creare il sistema di autenticazione e controllo degli accessi basato su ruoli (RBAC).
* **Componenti Coinvolti:** `Servizio Auth & Permessi`.
* **Risultato Concreto:** Un utente può registrarsi e fare login. Il sistema sa chi è e che ruolo ha (es. 'Commerciale', 'CMO'). Non c'è ancora un'interfaccia CRM visibile.

---

### **Fase 1: MVP Core - Il CRM per il Commerciale**
* **Obiettivo:** Sviluppare le funzionalità di base del CRM, rispettando i permessi definiti nella Fase 0.
* **Componenti Coinvolti:** `Servizio CRM Core`, `Frontend`.
* **Risultato Concreto:** Un utente con ruolo 'Commerciale' può loggarsi, creare/vedere/modificare **solo i propri** Contatti, Lead e Trattative.

---

### **Fase 2: MVP Analytics - La Dashboard Intelligente (Questo è l'MVP da presentare)**
* **Obiettivo:** Integrare i dati di analisi e creare le dashboard differenziate per ruolo.
* **Componenti Coinvolti:** `Servizio Dati (Analytics)`, `Frontend`.
* **Risultato Concreto:**
    1.  Viene implementato il processo per caricare (manualmente per l'MVP) i risultati degli script ETL nelle tabelle di riepilogo.
    2.  Il **Commerciale** vede una dashboard con i KPI e le analisi (RFM, etc.) relativi ai **propri clienti**.
    3.  Il **CMO** vede una dashboard con dati aggregati a livello aziendale.

---

### **Fase 3: Integrazione e Funzionalità Avanzate**
* **Obiettivo:** Integrare il microservizio di routing esistente e aggiungere altre funzionalità CRM avanzate.
* **Risultato Concreto:** Dalla scheda di un cliente o da una lista, un utente può avviare il calcolo della rotta ottimale di visite.

---

### **Fase 4: Evoluzione all'Architettura Event-Driven**
* **Obiettivo:** Migliorare la comunicazione tra servizi e l'automazione dei processi.
* **Risultato Concreto:** I servizi iniziano a emettere e consumare eventi (es. `trattativa_vinta`), aprendo la porta ad automazioni complesse (notifiche, integrazioni, etc.).