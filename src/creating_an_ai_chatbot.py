import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set your API key
client = OpenAI()

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
