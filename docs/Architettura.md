# Architettura di Sistema v2.0: Ecosistema NEXUS-CRM

Questa architettura a microservizi è progettata per la separazione delle competenze, la sicurezza e la scalabilità.

```text
              +----------------------------+
Utenti        |  Frontend (SvelteKit)      |
(Browser)     +-------------+--------------+
                            |
                            v
              +----------------------------+
              |   API Gateway (FastAPI)    |
              +-------------+--------------+
      +---------------------+---------------------+----------------------+
      |                     |                     |                      |
      v                     v                     v                      v
+--------------+   +----------------+   +----------------+   +----------------------+
|   Servizio   |   |    Servizio    |   | Servizio Dati  |   | Servizio di Routing  |
| Auth & Perm. |   |    CRM Core    |   |  (Analytics)   |   | (Esistente/Futuro)   |
+--------------+   +----------------+   +----------------+   +----------------------+
      ^                     ^                     ^                      ^
      |                     |                     |                      |
      +---------------------+---------------------+----------------------+
                            |
                            v
              +----------------------------+
              |   Database (PostgreSQL)    |
              +----------------------------+