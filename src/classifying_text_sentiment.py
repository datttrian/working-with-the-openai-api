import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set your API key
client = OpenAI()

# Create a request to the Completions endpoint
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="""Classify sentiment as negative, positive, or neutral:
    1. Unbelievably good!
    2. Shoes fell apart on the second use.
    3. The shoes look nice, but they aren't very comfortable.
    4. Can't wait to show them off!
  """,
    max_tokens=100,
)
print(response.choices[0].text)
