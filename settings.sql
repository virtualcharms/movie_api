-- settings.sql
CREATE DATABASE movie;
CREATE USER movieuser
WITH PASSWORD 'movie';
GRANT ALL PRIVILEGES ON DATABASE movie TO movieuser;