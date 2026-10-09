from langchain_google_genai  import ChatGoogleGenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenAI(model="gemini-pro")  # Initialize the ChatGoogleGenAI model with the desired model and parameters

result=model.invoke("what is the capital of india")  # Invoke the model with a prompt
print(result)
print(result.content)