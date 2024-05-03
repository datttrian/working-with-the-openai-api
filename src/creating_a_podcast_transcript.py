import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]


# Set your API key
client = OpenAI()

# Open the openai-audio.mp3 file
audio_file = open("openai-audio.mp3", "rb")

# Create a transcript from the audio file
response_transcript = client.audio.transcriptions.create(
    model="whisper-1", file=audio_file
)

# Extract and print the transcript text
print(response_transcript.text)
