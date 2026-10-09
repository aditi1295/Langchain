from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimenssions=32)
#vector kitne dimenssion ka hoga ye vo batata hai

result=embedding.embed_query("delhi is the capital of india")


print(str(result))