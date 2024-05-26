import json
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.microsoft.mssql.hooks.mssql import MsSqlHook
from datetime import datetime


def read_json(**kwargs):
    with open('etl/clicks.json', 'r') as f:
        data = json.load(f)
    return data


def upload_to_mssql(**kwargs):
    data = kwargs['ti'].xcom_pull(task_ids='read_json')

    # Convert the single JSON object to a list of dictionaries for pandas DataFrame
    data_list = [data]
    df = pd.DataFrame(data_list)

    hook = MsSqlHook(mssql_conn_id='mssql_default')
    conn = hook.get_conn()
    cursor = conn.cursor()

    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO ClickData (
                application_id, publisher_name, publisher_id, tracker_name, tracking_id,
                click_timestamp, click_datetime, click_ipv6, click_url_parameters, click_id,
                click_user_agent, ios_ifa, ios_ifv, android_id, google_aid, os_name,
                os_version, device_manufacturer, device_model, device_type, is_bot,
                country_iso_code, city
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, row.tolist())

    conn.commit()
    cursor.close()
    conn.close()


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 5, 26),
    'retries': 1,
}

with DAG('upload_json_to_mssql',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    read_json_task = PythonOperator(
        task_id='read_json',
        python_callable=read_json,
        provide_context=True,
    )

    upload_to_mssql_task = PythonOperator(
        task_id='upload_to_mssql',
        python_callable=upload_to_mssql,
        provide_context=True,
    )

    read_json_task >> upload_to_mssql_task
