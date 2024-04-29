import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Import the OpenAI client


# Create the OpenAI client and set your API key
client = OpenAI()

# Create a request to the Completions endpoint
response = client.completions.create(
    # Specify the correct model
    model="gpt-3.5-turbo-instruct",
    prompt="Who developed ChatGPT?",
)

print(response)


# Extract the model from response
print(response.model)

# Extract the total_tokens from response
if response.usage:
    print(response.usage.total_tokens)

# Extract the text from response
print(response.choices[0].text)
