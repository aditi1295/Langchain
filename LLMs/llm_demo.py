from langchain_openai import OpenAI
#isi se langchain ko pata chalta h ki openai se baat kaise krni h
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file


llm=OpenAI(model_name="gpt-3.5-turbo")  # Initialize the LLM with the desired model and parameters 

#invoke mode pr jake hit karega or usko ye question dega jo hame pucha hai or reply generate karega or vo reply hame vapas mil jayga

result=llm.invoke("what is the capital of india")

#reply ko hum result me store krke print kr daynge

print(result)