#method-1 api key ka use krna

from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="TinyLama/TinyLama-1.1B-Chat-v1.0",
    task="text-generation"
)


model=ChatHuggingFace(llm=llm) 
 # Initialize the ChatHuggingFace model with the desired model and parameters

result=model.invoke("what is the capital of india")  # Invoke the model with a prompt
print(result)
print(result.content)

