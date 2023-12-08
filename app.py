from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pydub import AudioSegment
from flask import send_file
from flask import jsonify
import io
import os
import pydub
import secrets  # Import the secrets module for generating secure API keys


app = Flask(__name__)
CORS(app)

# In-memory storage for uploaded audio files
audio_storage = {}  
user_api_keys = {} # Store user API keys
new_api_key = None  # Initialization of new_api_key



# Set the path to the FFmpeg executable
#FFMPEG_PATH = r'C:\Users\z004tu0x\AppData\Local\Programs\Python\Python311\Lib\ffmpeg\bin\'
#pydub.AudioSegment.converter = FFMPEG_PATH

#AudioSegment.converter = FFMPEG_PATH


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    global new_api_key
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Perform your authentication logic here
    if username == 'admin' and password == 'admin':
        # Check if the user already has an API key
        if username in user_api_keys:
            return jsonify({'success': True, 'message': 'Use your existing API key.', 'apiKey': None}), 200
        else:
            # Generate a new API key for the user
            new_api_key = secrets.token_urlsafe(32)
            user_api_keys[username] = new_api_key
            print(f"New API key generated for user {username}: {new_api_key}")
            return jsonify({'success': True, 'message': 'Your API key is: {}'.format(new_api_key), 'apiKey': new_api_key}), 200
    else:
        return jsonify({'success': False}), 401
    

    
@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    username = data.get('username')  # Assuming the username is sent from the frontend
    entered_api_key = data.get('apiKey')

    # Check if the user exists and the entered API key is correct
    if username in user_api_keys and user_api_keys[username] == entered_api_key:
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False}), 401


@app.route('/upload', methods=['POST'])
def upload_audio():
    # Check if the 'file' key is in the request.files dictionary
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # Check if the file is not empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded file to the in-memory storage
    if file:
        audio_content = file.read()
        #print(audio_content)

        # Print the volume of the uploaded audio
        initial_audio = AudioSegment.from_file(io.BytesIO(audio_content), format='mp3')
        print(f"Initial Volume: {initial_audio.dBFS} dBFS")

        audio_storage[file.filename] = audio_content
        return jsonify({'message': 'File uploaded successfully'}), 200



@app.route('/adjust', methods=['POST'])
def adjust_audio():
    # Get the desired volume level from the request JSON
    data = request.get_json()
    volume_level = data.get('volumeLevel')

    # Check if the volume level is valid
    if volume_level is None or not isinstance(volume_level, (int, float)):
        return jsonify({'error': 'Invalid volume level'}), 400

    # Get the latest uploaded audio file from audio_storage
    latest_audio_file = max(audio_storage.keys(), key=lambda x: audio_storage[x])

    # Retrieve the audio content of the latest uploaded file
    audio_content = audio_storage.get(latest_audio_file)

    # Check if the audio content is available
    if audio_content is None:
        return jsonify({'error': 'Audio file not found'}), 404

    # Implement your audio adjustment logic here
    # This is a placeholder, you need to replace it with your actual audio processing code
    adjusted_audio_content = adjust_audio_volume(audio_content, volume_level)

    # Update the audio content in the storage with the adjusted content
    audio_storage[latest_audio_file] = adjusted_audio_content


    return jsonify({'message': 'Audio adjusted successfully'}), 200

    #audio = AudioSegment.from_mp3(file_path)

def adjust_audio_volume(audio_content, volume_level):
    # Load audio from the provided content
    audio = AudioSegment.from_file(io.BytesIO(audio_content), format='mp3')
    
    # Debugging: Print the initial dBFS value
    print(f"Initial dBFS: {audio.dBFS}")
    
    # Adjust the volume
    adjusted_audio = audio + volume_level
    
    # Debugging: Print the adjusted dBFS value
    print(f"Adjusted dBFS: {adjusted_audio.dBFS}")
    
    # Export the adjusted audio as MP3 using the 'with' statement
    with io.BytesIO() as output_buffer:
        adjusted_audio.export(output_buffer, format='mp3')
        adjusted_audio_content = output_buffer.getvalue()
    
    return adjusted_audio_content



@app.route('/download', methods=['GET'])
def download_audio():
    # Check if there are no audio files uploaded
    if not audio_storage:
        return jsonify({'error': 'No audio files available for download'}), 404

    # Get the latest uploaded audio file from audio_storage
    latest_audio_file = max(audio_storage.keys(), default=None, key=lambda x: audio_storage[x])

    # Check if the audio content is available
    adjusted_audio_content = audio_storage.get(latest_audio_file)
    if adjusted_audio_content is None:
        return jsonify({'error': 'Audio file not found'}), 404

    # Provide the adjusted audio for download
    response = send_file(
        io.BytesIO(adjusted_audio_content),
        as_attachment=True,
        download_name='adjusted_new_audio.mp3',  # Change the file name as needed
        mimetype='audio/mp3',  # Change the mimetype based on the actual audio format
    )

    return response



if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=80)