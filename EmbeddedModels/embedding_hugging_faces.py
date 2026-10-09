from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",dimenssions=32)

documents=[
    "delhi is capital of india",
    "jaipur is capital of rajasthan",
    "paris is capital of france"
]

vector=embedding.embed_documents(documents)

print(str(vector))