# Airflow ELT Examples

This repository contains examples of ELT (Extract, Load, Transform) processes implemented using Apache Airflow. ELT processes are commonly used in data engineering to extract data from various sources, transform it into a usable format, and load it into a destination for analysis.

## ELT Processes

### 1. Open Food Facts ETL to MS SQL Server

#### Overview

This ELT process fetches product data from the Open Food Facts API, transforms it, and loads it into a Microsoft SQL Server database.

#### Components

- **DAG Name:** `open_food_facts_etl_to_mssql`
- **Description:** ETL process for fetching product data from Open Food Facts API, transforming it, and loading it into MS SQL Server.
- **Schedule:** Runs daily.
- **Dependencies:** No dependencies on past runs (catchup=False).
