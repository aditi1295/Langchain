#ye h mini project type h isme hum ek document laynge or usse related ek question puchneg to process ye hoga
#ki document or question dono ki embedding create karenge fir cosine  similarity rule lagaynge


from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large', dimenssions=300)

documents = [
"Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
"MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
"Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
"Rohit Sharma is known for his elegant batting and record-breaking double centuries."
"Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."]

query='tell me about virat kholi'

#jitni bar embeddings run kaorge mtlb hae bar embedding model se mang ke la rhe ho jo costly operation hai
#isliye document vali embedding ko store kiya jata h database me vo databse h vector database

doc_embeddings=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query) 

scores=cosine_similarity([query_embedding],doc_embeddings)[0]
index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]


print(query)
print(documents[index])
print("similarity score is :",score)