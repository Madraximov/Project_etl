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

#### Tasks

1. **fetch_data_task**: Fetches product data from the Open Food Facts API.
2. **transform_data_task**: Transforms the raw product data fetched by `fetch_data_task`.
3. **load_to_sql_task**: Loads transformed data into MS SQL Server.

### 2. Twitter Sentiment Analysis ETL to PostgreSQL

#### Overview

This ELT process collects tweets containing specific keywords, performs sentiment analysis, and stores the results in a PostgreSQL database.

#### Components

- **DAG Name:** `twitter_sentiment_analysis_etl_to_postgresql`
- **Description:** ETL process for collecting tweets, performing sentiment analysis, and storing results in PostgreSQL.
- **Schedule:** Runs hourly.
- **Dependencies:** No dependencies on past runs (catchup=False).

#### Tasks

1. **fetch_tweets_task**: Collects tweets containing specific keywords.
2. **perform_sentiment_analysis_task**: Analyzes the sentiment of collected tweets.
3. **load_to_postgresql_task**: Loads sentiment analysis results into PostgreSQL.

## Getting Started

To run these ELT processes locally or in your Airflow environment, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/airflow-elt-examples.git
