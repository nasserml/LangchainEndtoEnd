

from dotenv import load_dotenv # to load environment variables

load_dotenv() # laod all the environment variables from .env file and load GOOGLE_API_KEY

import streamlit as st # for the web development using streamlit
import os # is used to interact with the operating system
import pathlib # to interact with the file system
import textwrap # To wrap long text

import google.generativeai as genai # to load google gemini ai model 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # configure api key for google gemini ai model

# Fucntion to load google gemini pro vision Api and get response 