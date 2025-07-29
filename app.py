from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI

from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import streamlit as st
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

##envoirment variables call

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


## Langsmith tracking

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"] = "true"



#creating chatbot


prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please provide response to the user queries"),
        ("user","Question:{question}")
    ]
)

# streamlit framwork


st.title("Langchain Demo With Open AI API")
input_text=st.text_input("Search the topic you want")


#open AI LLM Call

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()


## chaiin

chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))


