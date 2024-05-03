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

# Create a transcription request using audio_file
audio_response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

# Create a request to the API to identify the language spoken
chat_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a languages specialist."},
        {
            "role": "user",
            "content": "Identify the language used in the following text: "
            + audio_response.text,
        },
    ],
)
print(chat_response.choices[0].message.content)
