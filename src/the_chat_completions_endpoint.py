import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set your API key
client = OpenAI()

# Create a request to the Chat Completions endpoint
response_chat = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=150,
    messages=[
        {"role": "system", "content": "You are a helpful data science tutor."},
        {
            "role": "user",
            "content": "What is the difference between a for loop and a while loop?",
        },
    ],
)

# Extract the assistant's text response
print(response_chat.choices[0].message.content)
