# NEXUS-CRM - Piattaforma Modulare per TSvapo

## Descrizione del Progetto

NEXUS-CRM è un sistema di Customer Relationship Management (CRM) progettato su un'architettura a microservizi per garantire scalabilità, manutenibilità e sicurezza. L'obiettivo è fornire al team di vendita e al management di TSvapo uno strumento potente per la gestione dei lead, delle trattative e dei clienti, arricchito da analisi dati avanzate.

Questo repository contiene il codice sorgente del frontend e dei vari microservizi che compongono la piattaforma.

## Architettura

Il sistema si basa su un'architettura a microservizi gestita tramite un API Gateway. Per una descrizione dettagliata dei componenti e del loro funzionamento, fare riferimento al documento [ARCHITECTURE.md](ARCHITECTURE.md).

## Roadmap di Sviluppo

Lo sviluppo seguirà una roadmap a fasi, focalizzata sulla consegna di valore incrementale. I dettagli delle fasi e degli obiettivi sono descritti nel documento [DEVELOPMENT_ROADMAP.md](DEVELOPMENT_ROADMAP.md).

## Stack Tecnologico Principale

* **Frontend:** SvelteKit
* **Backend (Microservizi):** FastAPI (Python)
* **Database:** PostgreSQL
* **Autenticazione Iniziale:** Supabase (per velocità di sviluppo MVP)
* **Hosting:** Hetzner Cloud VPS