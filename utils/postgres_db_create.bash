#!/usr/bin/env bash
sudo -u postgres psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    CREATE DATABASE carshop_db;
    CREATE USER carshop_user WITH PASSWORD 'password';
    ALTER ROLE carshop_user SET client_encoding TO 'utf8';
    ALTER ROLE carshop_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE carshop_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE carshop_db TO carshop_user;
    ALTER USER carshop_user CREATEDB;
EOSQL
