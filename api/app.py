from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    desvription = "A Simple API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path = "/openai"

)
#openai llm model
model = ChatOpenAI()
## ollama llm model

# llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an esay about{topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child")


add_routes(
    app,
    prompt1|model,
    path="/essay"
) 
add_routes(
    app,
    prompt2|model,
    path="/poem"
) 

if __name__ == "__main__":
    uvicorn.run(app,host= "localhost",port= 8000)