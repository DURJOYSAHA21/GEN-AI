from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["HF_HOME"] = r"F:\Gen-AI\huggingface"
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    
)

documents = [
    "What is the capital of France?",
    "What is the capital of Italy?",
    "What is the capital of Germany?"
]

text = "What is the capital of France?"

vector =embedding.embed_query(text)
vectors = embedding.embed_documents(documents)

print(vector)
print(vectors)