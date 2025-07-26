# 🧠 Mappatura Customer Journey ⇄ Moduli CRM Nexus

Questo documento mappa i touchpoint del Customer Journey (CJ) del reparto commerciale TSvapo con i moduli implementati nel CRM Nexus e definisce i principali KPI da monitorare in ciascuna fase.

---

## 🔁 Fasi del Customer Journey (CJ)

| Fase | Descrizione | Touchpoint principali | Modulo CRM correlato | KPI suggeriti |
|------|-------------|------------------------|-----------------------|----------------|
| **Awareness** | Il potenziale cliente scopre il brand TSvapo | Email, fiera, contatto social, sito web | `funnel_events` | Tasso apertura email, visite landing, conversione lead |
| **Consideration** | Il prospect valuta TSvapo come fornitore | Demo, call, follow-up, preventivo | `opportunity`, `funnel_events` | Conversione demo, risposta a preventivo, tempo medio contatto |
| **Decision** | Il cliente decide se acquistare | Trattativa commerciale, negoziazione | `sales_pipeline` | Probabilità chiusura, tempo di chiusura, % opportunità vinte |
| **Activation** | Primo ordine o test prodotto | Primo acquisto, onboarding | `visite`, `note`, `prodotti_venduti` | Tempo primo ordine, valore ordine iniziale, feedback |
| **Retention** | Il cliente viene fidelizzato | Riordini, supporto post-vendita | `funnel_events`, `note`, `interazioni` | Tasso riordino, NPS, durata media account |
| **Loyalty / Advocacy** | Il cliente diventa promotore del brand | Consigli, testimonianze, referral | (futuro: modulo `loyalty`) | % referral, recensioni, campagne loyalty |

---

## 📌 Dettagli Integrazione Moduli

### 📈 `opportunity`
- Rappresenta una potenziale trattativa (preventivo, demo, interesse)
- Collegata a `clienti` e assegnata a un `user`

### 🔄 `sales_pipeline`
- Registra lo stato corrente del cliente nel processo commerciale
- Tracciabile nel tempo tramite modifiche in `fase_corrente`

### 📅 `funnel_events`
- Ogni interazione significativa viene tracciata: email, call, demo, follow-up
- Può contenere anche l’esito dell’interazione (positivo/negativo)

### 🔍 `note`, `visite`, `interazioni`
- Supportano il tracking operativo e contestualizzano la relazione

---

## 🎯 KPI Prioritari da Visualizzare in Dashboard

| Nome KPI | Descrizione | Fonte dati |
|----------|-------------|-------------|
| Tempo medio chiusura opportunità | Media giorni tra creazione e chiusura | `opportunity` |
| Conversion rate per fase | % lead che passano alla fase successiva | `sales_pipeline`, `funnel_events` |
| Follow-up in ritardo | Eventi non aggiornati entro 48h | `funnel_events`, `note` |
| Riordini in 90gg | % clienti che hanno riordinato | `prodotti_venduti` |
| Churn rate stimato | Calcolato da segmentazione RFM | modulo `analytics` |

---

## 🚀 Prossimi step suggeriti

1. Implementare interfaccia per inserimento rapido `funnel_events`
2. Creare una dashboard funnel + andamento pipeline
3. Collegare dati CJ a sistema alert o automazioni RPA
4. Mappare un ID evento esterno (es. email automation o Fiera VapItaly)
5. Validare i KPI direttamente con il reparto commerciale

