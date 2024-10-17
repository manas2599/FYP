import os
import sys
import API
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API-KEY"] = API.OPENAI_API_KEY

query = sys.argv[1]
loader = TextLoader('article_1.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query, llm=ChatOpenAI))