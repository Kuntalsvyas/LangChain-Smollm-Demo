import os
import streamlit as st
from dotenv import load_dotenv

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tracers import LangChainTracer

# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT") or "smollm-demo"

# Streamlit UI
st.title("LangChain + Smollm Demo")
user_input = st.text_input("What question do you have in your mind?")

# LangChain components
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's question."),
    ("user", "Question: {question}")
])

llm = Ollama(model="smollm")
parser = StrOutputParser()

# Attach LangSmith tracer
tracer = LangChainTracer()
chain = (prompt | llm | parser).with_config({"callbacks": [tracer]})

# Inference
if user_input:
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": user_input})
        st.success("Here's your answer:")
        st.write(response)
