import unittest
from pydub import AudioSegment
from flask import send_file
from flask import json
from app import app
import io
import os


class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()

    def tearDown(self):
        # Clean up any files created during the tests
        for file_path in ["adjusted_new_audio.mp3", "test.mp3", "adjusted_new_audio.wav"]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_login_success(self):
        # Test the login route with correct credentials
        response = self.app.post('/login', json={'username': 'admin', 'password': 'admin'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('apiKey', data)

    def test_login_failure(self):
        # Test the login route with incorrect credentials
        response = self.app.post('/login', json={'username': 'admin', 'password': 'Admin'})  
        # Use 'admin' and 'Admin'
        self.assertEqual(response.status_code, 401)
        # Print or log the response content for further inspection
        print(response.get_data(as_text=True))


    def test_adjust_audio(self):
        # Use double backslashes to escape them or use a raw string
        # Option 1: Escaping backslashes
        with open("C:\\Users\\z004tu0x\\Desktop\\ai_coustics\\audio_processing_api\\Sample_Audio.mp3", "rb") as audio_file:
            # Upload the audio file
            self.app.post('/upload', data={'file': (io.BytesIO(audio_file.read()), 'test.mp3')})

        # Option 2: Using a raw string
        with open(r"C:\Users\z004tu0x\Desktop\ai_coustics\audio_processing_api\Sample_Audio.mp3", "rb") as audio_file:
            # Upload the audio file
            self.app.post('/upload', data={'file': (io.BytesIO(audio_file.read()), 'test.mp3')})

        # Test the adjust audio route with volume adjustment
        response = self.app.post('/adjust', json={'volumeLevel': 3})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)




if __name__ == '__main__':
    unittest.main()
