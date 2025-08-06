# 🧱 Sezione Tecnica Completa – NEXUS-CRM per TSvapo

## 🔧 Architettura Generale

```mermaid
graph TD
  A[Frontend - SvelteKit] --> B[API Layer - Node.js/Express]
  B --> C[Database - PostgreSQL]
  B --> D[Auth - Supabase Auth (RBAC + 2FA)]
  C --> E[Backup giornalieri su Scaleway S3]
  B --> F[Monitoring - Netdata]
  B --> G[CI/CD - GitHub Actions]
```

- **Frontend**: SvelteKit con componenti ottimizzati SSR
- **Backend/API**: Node.js con Express
- **Database**: PostgreSQL gestito con Prisma ORM
- **Autenticazione**: Supabase Auth + JWT + 2FA
- **Storage backup**: Scaleway S3 (criptato, ridondato)
- **Monitoring**: Netdata + UptimeRobot
- **CI/CD**: GitHub Actions (test, linting, build, deploy automatico)
- **Ambiente server**: Hetzner Cloud VPS, Ubuntu 22.04 LTS

---

## 🧪 CI/CD e Testing

- **GitHub Actions** per pipeline automatizzata:
  - `lint`, `build`, `test`, `deploy`
- **Test implementati**:
  - Unit test: Jest
  - E2E test: Playwright
  - Test di carico: k6
- **Copertura minima richiesta**: 85%

---

## 🧩 Moduli Core del Sistema

| Modulo               | Descrizione                                       | Stato |
|----------------------|---------------------------------------------------|-------|
| Auth & Accessi       | JWT + RBAC (Admin, Sales, Viewer)                 | ✅     |
| Clienti/Prospect     | CRUD clienti + filtri avanzati                    | ✅     |
| Visite Programmate   | Calendario e scheduling attività                  | ✅     |
| Dashboard            | KPI giornalieri, andamento vendite, lead status  | 🔄     |
| Modulo Percorsi      | Ottimizzazione geografica con Leaflet+OSRM        | 🔄     |
| Modulo Loyalty       | Pianificato (versione Q2 2026)                    | 🕓     |

---

## 🛠️ API Principali (REST)

| Metodo | Endpoint           | Descrizione                        | Autenticazione |
|--------|--------------------|------------------------------------|----------------|
| GET    | `/api/clients`     | Elenco clienti                     | ✅ JWT + RBAC   |
| POST   | `/api/clients`     | Crea un nuovo cliente              | ✅ JWT + RBAC   |
| GET    | `/api/clients/:id` | Dettaglio cliente                  | ✅ JWT + RBAC   |
| PUT    | `/api/clients/:id` | Modifica cliente                   | ✅ JWT + RBAC   |
| DELETE | `/api/clients/:id` | Elimina cliente                    | ✅ JWT + Admin  |
| GET    | `/api/visits`      | Elenco visite programmate          | ✅ JWT          |
| POST   | `/api/visits`      | Pianifica una nuova visita         | ✅ JWT          |

---

## 🗃️ Schema Database Esteso (PostgreSQL)

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT CHECK (role IN ('admin', 'sales', 'viewer')) NOT NULL
);

CREATE TABLE clients (
  id UUID PRIMARY KEY,
  company_name TEXT NOT NULL,
  vat_number TEXT UNIQUE,
  created_at TIMESTAMPTZ DEFAULT now(),
  created_by UUID REFERENCES users(id)
);

CREATE TABLE visits (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  client_id UUID REFERENCES clients(id),
  visit_date DATE NOT NULL,
  notes TEXT
);
```

---

## 🔐 Sicurezza e Conformità

- 🔑 Autenticazione: Supabase + JWT rinnovabile (12h)
- 🔐 2FA (OTP via email o app mobile)
- 🔒 Crittografia AES-256 per backup e dati sensibili
- 🛡️ Protezione DDoS con Cloudflare
- 📜 Audit log: modifiche critiche tracciate
- ⏳ Backup automatici giornalieri, conservazione: 30gg

---

## 📶 Monitoring & Recovery

- **Monitoring attivo** con Netdata
- Alert su Telegram/Email per: uptime, CPU, spazio disco
- Disaster recovery: ripristino completo < 30 min da backup
- Uptime target: **99.9%**
