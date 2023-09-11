from flask import Flask, request, render_template, send_from_directory
from gtts import gTTS
from werkzeug.utils import secure_filename
import os
import uuid

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    
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
    
    # Create a gTTS object
    tts = gTTS(text)
    
    # Save the audio with the unique filename
    tts.save(audio_file)
    
    return render_template('result.html', audio_file=unique_filename)


@app.route('/static/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename)


@app.route('/media/<path:filename>')
def media_files(filename):
    return send_from_directory('media', filename)

if __name__ == '__main__':
    app.run(debug=True)
