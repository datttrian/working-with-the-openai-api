from openai import OpenAI

# Set your API key
client = OpenAI()

# Create a request to the Moderation endpoint
response = client.moderations.create(
    model="text-moderation-latest",
    input="My favorite book is How to Kill a Mockingbird.",
)

print(response.results[0].category_scores)


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


# Set your API key
client = OpenAI()

# Open the audio.m4a file
audio_file = open("audio.m4a", "rb")

# Create a transcript from the audio file
response_transcript = client.audio.transcriptions.create(
    model="whisper-1", file=audio_file
)

print(response_transcript.text)


# Set your API key
client = OpenAI()

# Open the audio.m4a file
audio_file = open("audio.m4a", "rb")

# Create a translation from the audio file
response_translation = client.audio.translations.create(
    model="whisper-1", file=audio_file
)

# Extract and print the translated text
print(response_translation.text)


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


# Set your API key
client = OpenAI()

# Open the audio.wav file
audio_file = open("audio.wav", "rb")

# Create a transcription request using audio_file
audio_response = client.audio.transcriptions.create(
    model="whisper-1", file=audio_file
)

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


# Set your API key
client = OpenAI()

# Open the datacamp-q2-roadmap.mp3 file
audio_file = open("datacamp-q2-roadmap.mp3", "rb")

# Create a transcription request using audio_file
audio_response = client.audio.transcriptions.create(
    model="whisper-1", file=audio_file
)

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
