from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from.env
load_dotenv()

# create the Google Generative AI model

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

#Part 1 create a chat prompt template using a template string
print ("--------Prompt from Template ------------")
template = "Tell me a joke about {topic}"
prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({"topic": "cats"})
result = model.invoke(prompt)
print(result.content)

#Part 2 prompt with multiple placeholders

print ("\n--------Prompt with Multiple Placeholders------------\n")
template_multiple = """You are a helpful assistant.
Human: Tell me a {adjective} story about a {animal}"""
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "panda"})

result = model.invoke(prompt)
print(result.content)

#Part 3 prompt with system and human messages (using tuples)

print ("\n--------Prompt with System and Human Messages (Tuple)------------\n")
messages = [
    ("system", "You are a comedian who tells jokes about {topic}"),
    ("human", "Tell me {joke_count} jokes."),
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "dogs", "joke_count": "two"})
result = model.invoke(prompt)
print(result.content)