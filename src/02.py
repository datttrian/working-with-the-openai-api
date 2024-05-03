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


instruction = """Explain what this Python code does in one sentence:
import numpy as np

heights_dict = {"Mark": 1.76, "Steve": 1.88, "Adnan": 1.73}
heights = heights_dict.values()
print(np.mean(heights))
"""

# Create a request to the Chat Completions endpoint
response_chat = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Python programming assistant.",
        },
        {"role": "user", "content": instruction},
    ],
    max_tokens=100,
)
print(response_chat.choices[0].message.content)


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


messages = [{"role": "system", "content": "You are a helpful math tutor."}]
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

for q in user_msgs:
    print("User: ", q)

    # Create a dictionary for the user message from q and append to messages
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict)

    # Create the API request
    response_chat = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,  # type: ignore
        max_tokens=100,
    )

    # Convert the assistant's message to a dict and append to messages
    assistant_dict = {
        "role": "assistant",
        "content": response_chat.choices[0].message.content,
    }
    messages.append(assistant_dict)  # type: ignore
    print("Assistant: ", response_chat.choices[0].message.content, "\n")
