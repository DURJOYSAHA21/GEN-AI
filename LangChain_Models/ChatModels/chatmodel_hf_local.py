from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
import os


# Correct Hugging Face cache location
os.environ["HF_HOME"] = r"F:\Gen-AI\huggingface"


model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


pipe = pipeline(
    "text-generation",
    model=model_id,
    max_new_tokens=100,
    temperature=0.7
)


llm = HuggingFacePipeline(
    pipeline=pipe
)


result = llm.invoke(
   

"Question: What is the capital of France?"


)

print(result)