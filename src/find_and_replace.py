import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set your API key
client = OpenAI()

prompt = """Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine
or an electric motor. It has four wheels, and is designed to carry passengers
and/or cargo on roads or highways. Cars have become a ubiquitous part of modern
society, and are used for a wide variety of purposes, such as commuting,
travel, and transportation of goods. Cars are often associated with freedom,
independence, and mobility."""

# Create a request to the Completions endpoint
response = client.completions.create(
    model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=100
)

# Extract and print the response text
print(response.choices[0].text)
