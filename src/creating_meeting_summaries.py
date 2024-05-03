import os

import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]


# Set your API key
client = OpenAI()

# Open the datacamp-q2-roadmap.mp3 file
audio_file = open("datacamp-q2-roadmap.mp3", "rb")

# Create a transcription request using audio_file
audio_response = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

# Create a request to the API to summarize the transcript into bullet points
chat_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "List the courses that DataCamp will be making as "
            "bullet points." + audio_response.text,
        },
    ],
    max_tokens=100,
)
print(chat_response.choices[0].message.content)
