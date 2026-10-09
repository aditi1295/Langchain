


from typing import TypedDict



from langchain_huggingface import ChatHuggingFace ,HuggingFacePipeline


llm=HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    max_new_tokens=256,
    

)


model=ChatHuggingFace(llm=llm)

#schema for data ki hamar data kaisa structure hoga

class Review(TypedDict):
    summary: str
    sentiment: str

structured_model=model.with_structured_output(Review)  # Create a structured output model based on the Review schema

result =  structured_model.invoke("""The hardware is great, but the software feels bloated. There are
too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to
other brands. Hoping for a software update to fix this.""")


print(result)