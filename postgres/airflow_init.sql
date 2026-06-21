CREATE USER airflowuser WITH PASSWORD 'airflowpass';
CREATE DATABASE airflow_db OWNER airflowuser;
GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflowuser;
