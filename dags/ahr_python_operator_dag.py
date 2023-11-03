from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def my_python_function():
    print("Executing Python function")

# Define DAG
dag = DAG('python_operator_example', start_date=datetime(2023, 1, 1))

# Define Task
run_python_task = PythonOperator(
    task_id='run_python_function',
    python_callable=my_python_function,
    dag=dag
)
