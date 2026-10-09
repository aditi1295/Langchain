from langchain import ChatAntropic
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

model=ChatAntropic(model="claude-v1")  # Initialize the ChatAntropic model with the desired model and parameters


result=model.invoke("what is the capital of india")  # Invoke the model with a prompt
print(result)
print(result.content)