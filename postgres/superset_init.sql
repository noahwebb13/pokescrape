CREATE USER superset WITH PASSWORD 'superset';
CREATE DATABASE superset_db OWNER superset;
-- GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflowuser;

CREATE USER examples WITH PASSWORD 'examples';
CREATE DATABASE examples_db OWNER examples;