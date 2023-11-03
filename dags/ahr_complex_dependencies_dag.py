from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def task1():
    print("Task 1 executed")

def task2():
    print("Task 2 executed")

def task3():
    print("Task 3 executed")

# Define DAG
dag = DAG('complex_dag_example', start_date=datetime(2023, 1, 1))

# Define Tasks
start_task = DummyOperator(task_id='start', dag=dag)
task_1 = PythonOperator(task_id='task_1', python_callable=task1, dag=dag)
task_2 = PythonOperator(task_id='task_2', python_callable=task2, dag=dag)
task_3 = PythonOperator(task_id='task_3', python_callable=task3, dag=dag)
end_task = DummyOperator(task_id='end', dag=dag)

# Define Task Dependencies
start_task >> [task_1, task_2] >> task_3 >> end_task
