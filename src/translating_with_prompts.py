import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]


# Set your API key
client = OpenAI()

# Open the audio.wav file
audio_file = open("audio.wav", "rb")

# Write an appropriate prompt to help the model
prompt = "The transcript contains a discussion on a recent World Bank Report."

# Create a translation from the audio file
response_translation = client.audio.translations.create(
    model="whisper-1", file=audio_file, prompt=prompt
)
print(response_translation.text)
