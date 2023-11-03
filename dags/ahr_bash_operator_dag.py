from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Define DAG
dag = DAG('simple_bash_example', start_date=datetime(2023, 1, 1))

# Define Task
run_this = BashOperator(
    task_id='run_this',
    bash_command='echo "Hello, Airflow"',
    dag=dag
)
