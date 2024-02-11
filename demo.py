import streamlit as st
import openai
import speech_recognition as sr
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import io
import os
import wave
import pyaudio
from google.cloud import speech_v1p1beta1 as speech


# Set up OpenAI API key
openai.api_key = "OpenAI API key"

# Define function to generate code comments
def generate_comment(code_input, model_name):
    response = openai.Completion.create(
        model=model_name,
        prompt="/*{}*/".format(code_input),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    comment = response.choices[0].text
    return comment


# Define function to save comments to file
def save_comment(comment):
    with open("comments.txt", "a") as f:
        f.write(comment + "\n")

# Create Streamlit UI
st.title("ᴄᴏᴅᴇ ᴄᴏᴍᴍᴇɴᴛ ɢᴇɴᴇʀᴀᴛᴏʀ")

import streamlit as st
import speech_recognition as sr

# Function for searching
def search(query):
    # Perform search using the query
    # Replace this with your own search function
    search_results = ["Result 1", "Result 2", "Result 3"]
    return search_results

# Main code block
code_input = ""
use_voice_recognition = st.checkbox("Use Voice Recognition")

if use_voice_recognition:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Speak now")
        audio = r.listen(source)
    try:
        # Transcribe audio to text
        code_input = r.recognize_google(audio)
        st.write("You said: " + code_input)

        # Perform search with transcribed text
        search_results = search(code_input)
        st.write("Search results:")
        for result in search_results:
            st.write(result)

    except sr.UnknownValueError:
        st.write("Sorry, I didn't understand what you said")
    except sr.RequestError as e:
        st.write("Error: " + str(e))

else:
    code_input = st.text_area("What can I do for you!")
    
    # Perform search with manual text input
    search_results = search(code_input)
    st.write("Search results:")
    for result in search_results:
        st.write(result)

# Determine the programming language of the input code
lexer = get_lexer_by_name("text")
if "language" not in st.session_state:
    st.session_state["language"] = None

if st.session_state["language"] is not None:
    lexer = get_lexer_by_name(st.session_state["language"])
else:
    for lang in ["python", "java", "javascript", "html", "css"]:
        if lang in code_input.lower():
            lexer = get_lexer_by_name(lang)
            st.session_state["language"] = lang
            break

# # Highlight and display the input code
# formatter = HtmlFormatter(full=True, style="colorful")
# highlighted_code = highlight(code_input, lexer, formatter)
# style = "<style>{}</style>".format(formatter.get_style_defs())
# st.write(style + highlighted_code, unsafe_allow_html=True)

# Add language-specific comments
if st.session_state["language"] == "python":
    st.write("Consider using list comprehensions for more efficient code")

# Add a dropdown to select the AI model
model_names = ["text-davinci-002", "text-curie-001", "text-babbage-001"]
model_name = st.selectbox("Select AI model", model_names, index=0)

# Generate comments when button is clicked
if st.button("𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐂𝐨𝐦𝐦𝐞𝐧𝐭𝐬!🌈 "):
    comment = generate_comment(code_input, model_name)
    st.code(comment, language=st.session_state["language"])

    # Add a button to save the comment to file
    save_button = st.button("ꜱᴀᴠᴇ 𝐂𝐨𝐦𝐦𝐞𝐧𝐭𝐬!🌈 ")
    if save_button:
        save_comment(comment)
        st.write("Comment saved to file")


# Add a button to start recording audio
if st.button("ʀᴇᴄᴏʀᴅ ᴀᴜᴅɪᴏ"):
    # Record audio using PyAudio
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    audio_file = 'audio.wav'
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    # Save the recorded audio to a WAV file
    wf = wave.open(audio_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    # Display the recorded audio file
    st.audio(audio_file, format='audio/wav')
    # Add a button to transcribe the recorded audio
    if st.button("Transcribe Audio"):
        text = transcribe_audio(audio_file)
        st.write(text)
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        st.write("You said: {}".format(text))
        return text
    except sr.UnknownValueError:
        st.write("Could not understand audio")
    except sr.RequestError as e:
        st.write("Could not request results from Google Speech Recognition service; {0}".format(e))
    return ""
import streamlit as st
import speech_recognition as sr

# Set up SpeechRecognition
r = sr.Recognizer()

# Define the Streamlit app
def app():
    # Add a button to start speech recognition
    if st.button('Start recording'):
        with sr.Microphone() as source:
            # Listen for audio and convert it to text
            audio = r.listen(source)
            text = r.recognize_google(audio)
            st.write(f'Recognized text: {text}')

# Run the app
if __name__ == '__main__':
    app()


