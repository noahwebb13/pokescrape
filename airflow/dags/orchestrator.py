import os
import sys
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime, timedelta
from docker.types import Mount

HOST_PROJECT_ROOT = os.environ["HOST_PROJECT_ROOT"]

dbt_project_path = f"{HOST_PROJECT_ROOT}/dbt/my_project"
dbt_profiles_path = f"{HOST_PROJECT_ROOT}/dbt/profiles.yml"

sys.path.append('/opt/airflow/api-request')
# sys.path.append('/opt/api-request')

# def example_task():
#     print("This is an example task.\n")

def safe_main_callable():
    from insert_records import main
    return main()


default_args = {
    'description': 'DAG to orchestrate data',
    'start_date': datetime(2026, 5, 28),
    # 'catchup': False, 
}

dag = DAG(
    # dag_id='weather-api-orchestrator', 
    dag_id='weather_api_dbt_orchestrator', 
    default_args=default_args,
    schedule=timedelta(minutes=5),
    catchup=False
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_main_callable
    )
    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(
                # source='/home/noahwebb/repos/weather-data-project/dbt/my_project',
                source=dbt_project_path,
                target='/usr/app',
                type='bind',
                ),
            Mount(
                # source='/home/noahwebb/repos/weather-data-project/dbt/profiles.yml',
                source=dbt_profiles_path,
                target='/root/.dbt/profiles.yml',
                type='bind',
                ),

        ], 
        network_mode='weather-data-project_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success',

    )

    task1 >> task2