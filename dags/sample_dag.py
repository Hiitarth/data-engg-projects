from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define the Python function
def say_hello():
    print("Hel lo, HAstronome  r!!")

# Define the DAG
with DAG(
    dag_id="sample_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None
    catchup=False,
    description="A simple DAG to test Astronomer deployment",
    tags=["sample", "test"],
) as dag:


    # Create the task
    hello_task = PythonOperator(
        task_id="say_hello_task",
        python_callable=say_hello
    )


hello_task
