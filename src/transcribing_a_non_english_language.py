import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]


# Set your API key
client = OpenAI()

# Open the audio.m4a file
audio_file = open("audio.m4a", "rb")

# Create a transcript from the audio file
response_transcript = client.audio.transcriptions.create(
    model="whisper-1", file=audio_file
)
print(response_transcript.text)
