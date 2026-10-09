from langchain_openai import ChatOpenAI 

from dotenv import load_dotenv

load_dotenv()
#temprature paramater bhi set kr sakte hai
model=ChatOpenAI(models="gpt-4")  # Initialize the ChatOpenAI model with the desired model and parameters

result=model.invoke("what is the capital of india") 

print(result)
print(result.content)