# SQL-LLM-Gemini App

## Overview

This Streamlit web application, powered by the Google Gemini Pro model, enables users to retrieve SQL data by asking questions in English. The app integrates with a SQLite database named "STUDENT," with columns such as NAME, CLASS, SECTION, and MARKS. Users can input questions, and the Gemini Pro model generates SQL queries to fetch relevant data from the database.

## Configuration

1. Install the required libraries listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

2. Set up your environment variables by creating a `.env` file and adding your Google API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## Application Structure

- `app.py`: The main Streamlit app file that allows users to input questions and retrieve SQL data.
- `sql.py`: The script to set up and populate the SQLite database with sample records.

## Functionality

1. **Gemini Response Generation (`get_gemini_response`):**
   - The `get_gemini_response` function generates a response from the Gemini Pro model based on a question and a predefined prompt.

2. **SQL Query Execution (`read_sql_query`):**
   - The `read_sql_query` function reads and executes a provided SQL query on the specified SQLite database and returns the result as a list of tuples.

3. **Streamlit App (`app.py`):**
   - The Streamlit app provides a text input for users to enter their SQL-related questions.
   - Users can click the "Ask the question" button to trigger the Gemini Pro model to generate a SQL query.
   - The app then executes the generated SQL query on the SQLite database and displays the results.

## Sample Prompt

The predefined prompt guides users on how to structure their questions for the Gemini Pro model to generate accurate SQL queries.

```python
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, and MARKS.
    \n\nFor example,
    \nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - Tell me all the students studying in the Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS="Data Science";
    \nAlso, the SQL code should not have ``` in the beginning or end and the word "sql" in the output.
    """
]
```

## Database Setup

The `sql.py` script sets up an SQLite database named "student.db," creates a table named "STUDENT," inserts sample records, and displays the inserted records.

## Running the Application

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Interact with the app by entering SQL-related questions.

3. The app will generate SQL queries using the Gemini Pro model and display the results based on the SQLite database.
