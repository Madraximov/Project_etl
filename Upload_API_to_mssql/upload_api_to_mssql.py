from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.microsoft.mssql.operators.mssql import MsSqlOperator
from airflow.utils.dates import days_ago
import requests
import pandas as pd
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'open_food_facts_etl_to_mssql',
    default_args=default_args,
    description='ETL process for Open Food Facts API to MS SQL Server',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

# Example API endpoint
api_url = 'https://world.openfoodfacts.org/api/v0/product/737628064502.json'


# Function to fetch data from API
def fetch_data():
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()['product']
    else:
        raise Exception(f"Failed to fetch data from {api_url}. Status code: {response.status_code}")


# Example transformation function
def transform_data(raw_data):
    transformed_data = {
        'product_name': raw_data.get('product_name', ''),
        'categories': raw_data.get('categories', ''),
        'ingredients_text': raw_data.get('ingredients_text', ''),
        # Add more fields as needed
    }
    return transformed_data


# Function to load data into MS SQL Server
def load_to_sql(**kwargs):
    transformed_data = kwargs['ti'].xcom_pull(task_ids='transform_data_task')

    # Example: Connect to MS SQL Server
    conn_str = 'mssql+pyodbc://Aza:<Kk123456>@<NOTHING>/<airflow_db>?driver=ODBC+Driver+17+for+SQL+Server'
    engine = create_engine(conn_str)

    # Example: Create a pandas DataFrame from transformed data
    df = pd.DataFrame([transformed_data])

    # Example: Write DataFrame to MS SQL Server table
    df.to_sql('open_food_facts_data', con=engine, if_exists='append', index=False)
    print("Data loaded into MS SQL Server successfully.")


# Define tasks in the DAG
fetch_data_task = PythonOperator(
    task_id='fetch_data_task',
    python_callable=fetch_data,
    dag=dag,
)

transform_data_task = PythonOperator(
    task_id='transform_data_task',
    python_callable=transform_data,
    provide_context=True,
    dag=dag,
)

load_to_sql_task = PythonOperator(
    task_id='load_to_sql_task',
    python_callable=load_to_sql,
    provide_context=True,
    dag=dag,
)

# Define task dependencies
fetch_data_task >> transform_data_task >> load_to_sql_task
