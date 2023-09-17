# Incomplete and Paused Airflow ETL Twitter Project

This project represents an ongoing initiative to create an Extract, Transform, Load (ETL) pipeline using Apache Airflow to collect tweets related to the search query "data science" from Twitter's API. However, it is essential to note that this project is currently incomplete and has been paused for further development.

## Project Overview

The project's ultimate goal is to automate the extraction, transformation, and loading of Twitter data into a structured format for subsequent analysis. The planned workflow includes the following steps:

1. **Data Extraction from Twitter API**:
   - Utilizing the Twitter API to retrieve recent tweets containing the search query "data science."
   - Implementing pagination to handle a substantial volume of tweets.

2. **Data Transformation**:
   - Converting the raw JSON response from the Twitter API into a structured format.
   - Extracting essential tweet attributes such as author ID, conversation ID, creation timestamp, tweet ID, language, and tweet text.
   - Collecting additional user-related information like user ID, name, username, and account creation timestamp.

3. **Data Loading**:
   - Storing the transformed data in a designated database or storage system for subsequent analysis.

4. **Scheduling and Monitoring**:
   - Leveraging Apache Airflow for scheduling and automation, enabling periodic execution of the ETL pipeline to retrieve new tweets.
   - Implementing monitoring and logging features to track the pipeline's execution.

## Components Used

- **Apache Airflow**: The primary platform for authoring, scheduling, and monitoring workflows.
- **Twitter API**: Access to Twitter's API is required to fetch tweets.
- **Python**: The scripting language used for data manipulation and workflow orchestration.
- **JSON**: Used for handling and transforming data in JSON format.

## Workflow (Planned)

1. The ETL process begins by defining the query, date range, and the required tweet and user fields.
2. A URL is constructed with the specified parameters and authorization headers.
3. A GET request is sent to the Twitter API, retrieving a JSON response containing tweets.
4. The JSON response is transformed into a structured format.
5. The transformed data is stored or loaded into a database for analysis.
6. The process is designed to be paginated to retrieve more tweets when a "next_token" is present in the API response.
7. Apache Airflow is set up to schedule and automate the ETL process at predefined intervals.

## Project Status

As of now, this project remains incomplete and paused. Further development and refinement of the ETL pipeline are required to achieve the desired automation and functionality. Incomplete aspects of the project include error handling, production-ready logging, and a secure mechanism for storing Twitter API credentials (bearer token).

The project's future progress and completion will depend on the priorities and resources allocated to it.
