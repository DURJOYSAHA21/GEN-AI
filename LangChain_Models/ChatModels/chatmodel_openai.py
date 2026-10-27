from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI = ChatOpenAI(model="gpt-4") #adding the model parameter to specify which OpenAI model to use. In this case, it is set to "gpt-4" and temperature will help to contorl the creativity of the model and max_completion_tokens will limit the number of tokens in the response.
result = model.invoke("What is the capital of France?")

print(result)

