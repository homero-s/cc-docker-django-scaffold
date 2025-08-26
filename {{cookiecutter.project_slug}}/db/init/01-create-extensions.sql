-- Optional: enable useful extensions in the default DB
-- These statements are safe to run if the extensions already exist.
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
