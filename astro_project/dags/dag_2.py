from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("This one is the second 2 dag!")

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='hello_astro_dag',
    schedule='@daily', 
    default_args=default_args,
    catchup=False,
    tags=['example'],
) as dag:

    hello_task = PythonOperator(
        task_id='say_hello_task',
        python_callable=say_hello,
    )

hello_task
