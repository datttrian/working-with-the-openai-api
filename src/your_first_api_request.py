import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Create the OpenAI client and set your API key
client = OpenAI()

# Create a request to the Completions endpoint
response = client.completions.create(
    # Specify the correct model
    model="gpt-3.5-turbo-instruct",
    prompt="Who developed ChatGPT?",
)
print(response)
