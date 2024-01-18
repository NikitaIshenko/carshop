#!/usr/bin/env bash
sudo -u postgres psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    DROP DATABASE IF EXISTS carshop_db;
    DROP DATABASE IF EXISTS test_carshop_db;
    DROP USER IF EXISTS carshop_user;
    DROP USER IF EXISTS test_carshop_db;
EOSQL
