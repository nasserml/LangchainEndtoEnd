# Conversational Q&A Chatbot

This project implements a conversational Q&A chatbot using Streamlit and OpenAI's language model to engage in interactive conversations.

## Overview
The folder contains the necessary code to build and run a simple conversational chatbot capable of answering user queries using OpenAI's language model. The code is structured as follows:

- `app.py`: Contains the Streamlit-based user interface for the conversational chatbot.
- `langchain.ipynb`: A Jupyter Notebook demonstrating the underlying logic and interaction with the OpenAI model.
- `requirements.txt`: Lists the required Python packages for running the application.

## Project Details
The primary component, `app.py`, establishes the user interface to interact with the chatbot. It leverages the Streamlit framework to take user input, send queries to the OpenAI language model, and display the model's responses in a conversation-like interface.

## Usage
To run the conversational Q&A chatbot:
1. Clone this repository.
2. Install the required Python packages listed in `requirements.txt`.
3. Configure the necessary environment variables (using `.env`) and set up an API key for OpenAI.

Execute the `app.py` script to initiate the Streamlit-based UI for interacting with the chatbot. Enter queries in the provided input field and click the 'Ask the question' button to see the chatbot's response.

### Note
Please note that the `langchain.ipynb` Jupyter Notebook serves as a supporting file, offering insights into the logic and interaction with the OpenAI language model. It provides a deeper understanding of the chatbot's functionality.

This project is intended for educational purposes, showcasing the implementation of a basic conversational chatbot and the interaction with OpenAI's language model.

---
Kindly refer to the individual scripts and notebook for specific details and usage instructions. Always adhere to the usage terms and conditions of the OpenAI API.
