# User
`noahwebb`

# Password
`*************ux*$`

# In PowerShell (or VS Code Terminal) to Launch Ubuntu
```bash
wsl.exe -d Ubuntu
```

---

# In Terminal in VS Code

## Upgrade Packages
```bash
sudo apt update
sudo apt full-upgrade
```

## Quick Commands
> Explain these later

```bash
docker-compose up
cd repos/weather-data-project/api-request
```

## Retrieve temporary airflow password
```bash
docker-compose logs af 2>&1 | grep -i "password\|admin_user\|temporary"
```


## Execute the Service
> Use the PostgreSQL command  
> (might get Docker permission denied)

```bash
cd repos/weather-data-project
docker-compose exec db psql -U db_user -d db
```

## Start the Container
> Used this command after moving the YAML file to a new location and the service was already running

```bash
docker start postgres_container
```

---

# Viewing Database Using Terminal

## List Databases
```linux
\l
```

## Find Schemas
```linux
\dn
```

## Connect to db
```linux
\c db
```

## list tables in public schema
```linux
\dt pubic.*
```

## Installing virtual environment package
```linux
sudo apt install python3.14-venv
```


## Tuncating tables/using SQL commands in postgres terminal
These are commands and results pasted below: 
```sql
db=# truncate table dev.raw_weather-data;
ERROR:  syntax error at or near "-"
LINE 1: truncate table dev.raw_weather-data;
                                      ^
db=# truncate table dev.raw_weather_data;
TRUNCATE TABLE
db=# select * from dev.raw_weather_data;
 id | city | temperature | weather_descriptions | wind_speed | time | inserted_at | utc_offset 
----+------+-------------+----------------------+------------+------+-------------+------------
(0 rows)

db=# 

```


## Viewing permissions to the postgres folder
```linux
ls -l /home/noahwebb/repos/weather-data-project/postgres
```


## Adding permissions to the postgres folder
```linux
sudo chmod -R g+rw /home/noahwebb/repos/weather-data-project/postgres
sudo chgrp -R $USER /home/noahwebb/repos/weather-data-project/postgres
sudo chmod -R 770 /home/noahwebb/repos/weather-data-project/postgres

```

## Removing postgres data folder and replacing it, docker-compose up
```linux
docker-compose down
rm -rf ./postgres/data
docker-compose up

```

## View useer permissions
```linux
docker-compose exec db psql -U db_user -d db
\l
\du
```

## Checking permissions on airflow_container and dags folder
```linux
docker exec -it airflow_container bash
ls /opt/airflow/dags
```

## initializing dbt then debugging 
change the "command" from "init my_project" to "debug"
```yamml
  dbt:
    container_name: dbt_container
    image: ghcr.io/dbt-labs/dbt-postgres:1.9.latest
    volumes:
      - ./dbt:/usr/app
    working_dir: /usr/app
    depends_on:
      - db
    networks:
      - my-network
    command: init my_project

```


## Copying dbt profiles.yml from a container to the host machine

```linux
docker cp c9593310f0e1:/root/.dbt/profiles.yml /home/noahwebb/repos/weather-data-project/dbt
```

Copies the `profiles.yml` file from the Docker container to the local `dbt` folder. This file contains dbt database connection settings.


























## Troubleshooting docker-compose up
```linux

noahwebb@Noah-Gaming:~/repos/weather-data-project$ docker-compose down
[+] down 3/3
 ✔ Container airflow_container             Removed                                                                                          0.0s
 ✔ Container postgres_container            Removed                                                                                          0.0s
 ✔ Network weather-data-project_my-network Removed                                                                                          0.3s
noahwebb@Noah-Gaming:~/repos/weather-data-project$ rm -rf .postgres/data
noahwebb@Noah-Gaming:~/repos/weather-data-project$ docker-compose up
[+] up 3/3
 ✔ Network weather-data-project_my-network Created                                                                                          0.0s
 ✔ Container postgres_container            Created                                                                                          0.1s
 ✔ Container airflow_container             Created                                                                                          0.1s
Attaching to airflow_container, postgres_container
postgres_container  | The files belonging to this database system will be owned by user "postgres".
postgres_container  | This user must also own the server process.
postgres_container  | 
postgres_container  | The database cluster will be initialized with locale "en_US.utf8".
postgres_container  | The default database encoding has accordingly been set to "UTF8".
postgres_container  | The default text search configuration will be set to "english".
postgres_container  | 
postgres_container  | Data page checksums are disabled.
postgres_container  | 
postgres_container  | initdb: error: directory "/var/lib/postgresql/data" exists but is not empty
postgres_container  | If you want to create a new database system, either remove or empty
postgres_container  | the directory "/var/lib/postgresql/data" or run initdb
postgres_container  | with an argument other than "/var/lib/postgresql/data".
postgres_container exited with code 1
airflow_container   | 
airflow_container   | airflow command error: the following arguments are required: GROUP_OR_COMMAND, see help above.
airflow_container   | Usage: airflow [-h] GROUP_OR_COMMAND ...
airflow_container   | 
airflow_container   | Positional Arguments:
airflow_container   |   GROUP_OR_COMMAND
airflow_container   | 
airflow_container   |     Groups
airflow_container   |       assets            Manage assets
airflow_container   |       aws-auth-manager  Manage resources used by AWS auth manager
airflow_container   |       backfill          Manage backfills
airflow_container   |       celery            Celery components
airflow_container   |       config            View configuration
airflow_container   |       connections       Manage connections
airflow_container   |       dags              Manage DAGs
airflow_container   |       db                Database operations
airflow_container   |       db-manager        Manage externally connected database managers
airflow_container   |       fab-db            Manage FAB
airflow_container   |       jobs              Manage jobs
airflow_container   |       kubernetes        Tools to help run the KubernetesExecutor
airflow_container   |       pools             Manage pools
airflow_container   |       providers         Display providers
airflow_container   |       roles             Manage roles
airflow_container   |       tasks             Manage tasks
airflow_container   |       teams             Manage teams
airflow_container   |       users             Manage users
airflow_container   |       variables         Manage variables
airflow_container   | 
airflow_container   |     Commands:
airflow_container   |       api-server        Start an Airflow API server instance
airflow_container   |       cheat-sheet       Display cheat sheet
airflow_container   |       dag-processor     Start a dag processor instance
airflow_container   |       info              Show information about current Airflow and environment
airflow_container   |       kerberos          Start a kerberos ticket renewer
airflow_container   |       permissions-cleanup
airflow_container   |                         Clean up DAG permissions in Flask-AppBuilder tables
airflow_container   |       plugins           Dump information about loaded plugins
airflow_container   |       rotate-fernet-key
airflow_container   |                         Rotate encrypted connection credentials and variables
airflow_container   |       scheduler         Start a scheduler instance
airflow_container   |       standalone        Run an all-in-one copy of Airflow
airflow_container   |       sync-perm         Update permissions for existing roles and optionally
airflow_container   |                         DAGs
airflow_container   |       triggerer         Start a triggerer instance
airflow_container   |       version           Show the version
airflow_container   | 
airflow_container   | Options:
airflow_container   |   -h, --help            show this help message and exit
airflow_container exited with code 2
noahwebb@Noah-Gaming:~/repos/weather-data-project$ 

v View in Docker Desktop   o View Config   w Enable Watch   d Detach

```

