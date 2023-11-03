from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def parameterized_task(param):
    print(f"Executing parameterized task with parameter: {param}")

# Define DAG
dag = DAG('parameterized_dag_example', start_date=datetime(2023, 1, 1))

# Define Task
run_parameterized_task = PythonOperator(
    task_id='run_parameterized_task',
    python_callable=parameterized_task,
    op_args=['example_parameter'],
    dag=dag
)
