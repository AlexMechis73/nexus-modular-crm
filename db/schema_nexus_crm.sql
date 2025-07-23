
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
