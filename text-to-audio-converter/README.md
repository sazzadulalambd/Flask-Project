# Text to Audio Converter Web Application

This is a simple web application built with Flask that allows users to convert text to audio files (e.g., MP3). Users can input text, and the application will generate an audio file with the text converted to speech.

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python (3.6 or higher)
- Virtual environment (optional but recommended)

## Getting Started

Follow these steps to set up and run the Text to Audio Converter:

1. **Clone the repository to your local machine:**

```bash
   git clone https://github.com/sazzadulalambd/Flask-Project.git
   cd text-to-audio-converter
```

2. **(Optional) Create and activate a virtual environment:**

```bash
python -m venv .venv
On Unix or MacOS, use: source .venv/bin/activate
On Windows, use: .venv\Scripts\activate
```

3. **Install dependencies from `requirements.txt` file using pip**
Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. **Run the app with this command in terminal**
Run the Flask application:

```bash
python app.py
```

Access the web application in your web browser at http://localhost:5000 or http://127.0.0.1:5000.

# Usage

1. Enter the text you want to convert to audio in the input form on the homepage.
2. Click the "Convert" button.
3. The application will generate an audio file with the converted text, and you can listen to it on the result page.

# Folder Structure
- app.py: The main Flask application script.
- templates/: HTML templates for the application.
- static/: Static assets such as CSS files.
- media/: Directory to store generated audio files.
- requirements.txt: List of Python dependencies.
- README.md: Project documentation.

# Customization
You can customize the application further by modifying the templates, adding additional styling (CSS), or enhancing the functionality.

# Deployment

To deploy this application in a production environment, you can use a web server like Nginx or Apache. Refer to the Flask documentation for deployment options.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Author

- Sazzadul Alam Shawon
- GitHub: [Author GitHub Profile](https://github.com/sazzadulalambd)
- Website: sazzad.naynab.com

# Acknowledgments

- Special thanks to the Flask and gTTS communities for their contributions to open-source software.

