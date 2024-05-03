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
    prompt=(
        "Categorize the following list of companies as either Tech, "
        "Energy, Luxury Goods, or Investment: Apple, Microsoft, Saudi Aramco, "
        "Alphabet, Amazon, Berkshire Hathaway, NVIDIA, Meta, Tesla, LVMH"
    ),
    max_tokens=100,
    temperature=0.5,
)
print(response.choices[0].text)
