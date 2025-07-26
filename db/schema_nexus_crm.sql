
-- Schema PostgreSQL per NEXUS-CRM

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

-- 🔽 [ESTENSIONE FUNNEL E PIPELINE] 🔽

-- 🔧 ESTENSIONE SCHEMA POSTGRESQL / PRISMA per CRM Funnel & Pipeline

-- 🗂️ Opportunità commerciali
CREATE TABLE opportunity (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL REFERENCES clienti(id) ON DELETE CASCADE,
    titolo VARCHAR(100) NOT NULL,
    descrizione TEXT,
    valore_potenziale DECIMAL(10, 2),
    prob_successo INTEGER CHECK (prob_successo BETWEEN 0 AND 100),
    data_creazione TIMESTAMP DEFAULT NOW(),
    data_chiusura_prevista DATE,
    stato VARCHAR(20) CHECK (stato IN ('aperta', 'in corso', 'chiusa', 'persa')),
    assegnato_a INTEGER REFERENCES users(id)
);

-- 📈 Pipeline di vendita (stato aggregato del cliente nel funnel)
CREATE TABLE sales_pipeline (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL REFERENCES clienti(id) ON DELETE CASCADE,
    fase_corrente VARCHAR(50),  -- es. "Lead Qualificato", "Demo inviata", "In trattativa"
    data_ingresso_fase TIMESTAMP DEFAULT NOW(),
    owner_id INTEGER REFERENCES users(id),
    note TEXT
);

-- 🧭 Eventi funnel (timeline dettagliata di touchpoint)
CREATE TABLE funnel_events (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER NOT NULL REFERENCES clienti(id) ON DELETE CASCADE,
    tipo_evento VARCHAR(50), -- es. "email inviata", "demo eseguita", "chiamata completata"
    descrizione TEXT,
    data_evento TIMESTAMP DEFAULT NOW(),
    esito VARCHAR(20) -- es. "positivo", "negativo", "n/a"
);
