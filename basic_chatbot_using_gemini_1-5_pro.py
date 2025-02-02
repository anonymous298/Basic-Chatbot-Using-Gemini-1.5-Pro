import os
from pandas.core.series import StructAccessor
import streamlit as st

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Loading the API Key from Google Gemini
SEC_KEY = os.getenv('GOOGLE_GEMINI_API')

st.title('Basic Chatbot Using Google Gemini 1.5 pro')
user_input = st.text_input('What do you want to ask? ')

# loading Our LLM
llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-pro-latest',
    api_key=SEC_KEY,
    temperature=0.3
)

# Creating a ChatPromptTemplate for our LLM
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are an Intelligent Assistant Jarvis'),
        ('user', 'Question: {question} in 100 words')
    ]
)

# Creating a Chain for our ChatBot
chain = prompt | llm | StrOutputParser()


if st.button('Ask'):
    response = chain.invoke({'question' : user_input}) # Invoking the Chain with the users input
    st.write(response)