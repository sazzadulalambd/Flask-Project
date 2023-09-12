from flask import Flask, request, render_template, send_from_directory
import pyttsx3
from werkzeug.utils import secure_filename
import os
import uuid

app = Flask(__name__)

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Get a list of available voices
voices = engine.getProperty('voices')

@app.route('/')
def home():
    return render_template('index.html', voices=voices)

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    selected_voice = request.form['voice']
    speech_speed = float(request.form['speed'])
    
    # Configure the speech speed (rate)
    engine.setProperty('rate', speech_speed * 150)  # Adjust the multiplier for your preference
    
    # Set the selected voice based on the user's choice
    engine.setProperty('voice', selected_voice)
    
    # Split the input text into words
    words = text.split()
    
    # Take a maximum of 3 words from the input text
    selected_words = ' '.join(words[:3])
    
    # Generate a unique filename using the selected words
    filename_base = secure_filename(selected_words)
    unique_filename = f"{filename_base}.mp3"
    
    # Check if the file already exists
    audio_file = os.path.join('media', unique_filename)
    counter = 1
    while os.path.exists(audio_file):
        # Append (1), (2), etc., to the filename if it already exists
        unique_filename = f"{filename_base} ({counter}).mp3"
        audio_file = os.path.join('media', unique_filename)
        counter += 1

    # Convert text to speech
    engine.save_to_file(text, audio_file)
    engine.runAndWait()
    
    return render_template('result.html', audio_file=unique_filename, voices=voices)


@app.route('/static/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename)


@app.route('/media/<path:filename>')
def media_files(filename):
    return send_from_directory('media', filename)

if __name__ == '__main__':
    app.run(debug=True)
