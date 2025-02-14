from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.timezone import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email': ['jacob.sigling@avanade.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'trigger_rule': 'all_success',
}

with DAG(
        dag_id='fifth_dag',
        default_args=default_args,
        description='My first DAG',
        schedule_interval='@daily',
        catchup=False,
) as dag:

    task1 = EmptyOperator(task_id='Task1')
    task2 = EmptyOperator(task_id='Task2')
    task3 = EmptyOperator(task_id='Task3')

    task1 >> task2 >> task3
