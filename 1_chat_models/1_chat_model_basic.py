# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os 
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
# model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))

# # Invoke the model with a message
# result = model.invoke("What is 81 divided by 9?")
# print("Full result:")
# print(result)
# print("Content only:")
# print(result.content)
# Create a ChatGoogleGemini model
google_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Invoke the model with a message
google_result = google_model.invoke("What is 81 divided by 9?")
print("Google Full result:")
print(google_result)
print("Google Content only:")
print(google_result.content)