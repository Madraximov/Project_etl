# Open Food Facts ETL to MS SQL Server

This Airflow DAG (Directed Acyclic Graph) automates the Extract, Transform, Load (ETL) process from the Open Food Facts API to a Microsoft SQL Server database.

## DAG Overview

- **DAG Name:** open_food_facts_etl_to_mssql
- **Description:** ETL process for fetching product data from Open Food Facts API, transforming it, and loading it into MS SQL Server.
- **Schedule:** Runs daily.
- **Start Date:** One day ago from the current date.
- **Dependencies:** No dependencies on past runs (catchup=False).

## Tasks

### 1. fetch_data_task

- **Task ID:** fetch_data_task
- **Operator:** PythonOperator
- **Function:** Fetches product data from the Open Food Facts API.
- **Dependencies:** None

### 2. transform_data_task

- **Task ID:** transform_data_task
- **Operator:** PythonOperator
- **Function:** Transforms the raw product data fetched by `fetch_data_task`.
- **Dependencies:** Depends on `fetch_data_task`.

### 3. load_to_sql_task

- **Task ID:** load_to_sql_task
- **Operator:** PythonOperator
- **Function:** Loads transformed data into MS SQL Server.
- **Dependencies:** Depends on `transform_data_task`.

## Default Arguments

- **Owner:** airflow
- **Retries:** 1
- **Retry Delay:** 5 minutes
- **Email Notifications:** Disabled for failures and retries.

## Example API Endpoint

- **API URL:** [https://world.openfoodfacts.org/api/v0/product/737628064502.json](https://world.openfoodfacts.org/api/v0/product/737628064502.json)
- **Description:** Example of the endpoint used to fetch product data.

## Connection String for MS SQL Server

- **Connection String:** 
- **Description:** Connects to MS SQL Server for data insertion.

## Example Transformation Function

- **Function:** `transform_data`
- **Purpose:** Transforms raw JSON data into a structured format suitable for insertion into a database.
- **Fields Extracted:** `product_name`, `categories`, `ingredients_text`, etc.

## Notes

- Ensure that the MS SQL Server credentials and database details in the connection string (`conn_str`) are correctly configured.
- Adjust the API endpoint (`api_url`) and transformation logic (`transform_data` function) as per your specific requirements.

---

This DAG is designed to automate the process of updating product data from Open Food Facts into MS SQL Server on a daily basis. Adjustments can be made to enhance error handling, logging, and scalability based on operational needs.
