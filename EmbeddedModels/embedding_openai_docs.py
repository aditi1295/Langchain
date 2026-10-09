from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimenssions=32)
#vector kitne dimenssion ka hoga ye vo batata hai
#multiple queries ko ek sath embedding krne ke liye
documents=[
    "delhi is capital of india",
    "jaipur is capital of rajasthan",
    "paris is capital of france"
]

result=embedding.embed_documents(documents)


print(str(result))

