import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set your API key
client = OpenAI()

response_chat = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # Add a user and assistant message for in-context learning
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Python programming tutor.",
        },
        {"role": "user", "content": "Explain what the min() function does."},
        {
            "role": "assistant",
            "content": "The min() function returns the smallest item from an "
            "iterable.",
        },
        {"role": "user", "content": "Explain what the type() function does."},
    ],
)
print(response_chat.choices[0].message.content)
