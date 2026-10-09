#method-2 locally download krke chalna

from langchain_huggingface import ChatHuggingFace ,HuggingFacePipeline


llm=HuggingFacePipeline.from_model_id(
    repo_id='TinyLama/TinyLama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=256,
    )

)

model=ChatHuggingFace(llm=llm)  

result=model.invoke("what is the capital of india")  # Invoke the model with a prompt
print(result)
print(result.content)