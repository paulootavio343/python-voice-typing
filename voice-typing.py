from pathlib import Path  # Import module to get system paths

import keyboard  # Import module to handle keyboard inputs
import speech_recognition as sr  # Import module for speech recognition
import whisper  # Import module for transcribing audio

# Path to save Whisper models
download_path = Path() / 'whisper_models'

# Define the Whisper model to be used
# Available models and their sizes can be found here: https://github.com/openai/whisper
whisper_model = whisper.load_model("base.en", download_root=download_path)

# Initialize a speech recognizer object
recognizer = sr.Recognizer()

# Set pause and phrase thresholds for speech recognition
recognizer.pause_threshold = 1  # Pause detection after 1 second of silence
recognizer.phrase_threshold = 1  # Minimum phrase length to be recognized

# Calibrate the recognizer to ambient noise in microphone
with sr.Microphone() as mic:
    recognizer.adjust_for_ambient_noise(mic, duration=2)

    # Enter an infinite loop to continuously transcribe audio
    while True:
        print('Standby...')  # Indicate waiting state
        keyboard.wait('ctrl')  # Wait for user to press Ctrl key

        # Try to recognize speech from the microphone for 2 seconds
        try:
            audio = recognizer.listen(mic, timeout=2)
        except sr.WaitTimeoutError:
            print('No audio received, continuing...')  # Handle timeout error
            continue

        # Save the recognized audio to a WAV file
        with open("audio.wav", "wb") as f:
            f.write(audio.get_wav_data())
            f.close()

        # Transcribe the audio using the Whisper model
        whisper_output = whisper_model.transcribe("audio.wav")
        whisper_text = whisper_output["text"]

        # If text is transcribed successfully
        if whisper_text:
            try:
                # Attempt to type the transcribed text with a delay between each character
                # Increase the delay if the program crashes to avoid overwhelming your system
                keyboard.write(whisper_text, delay=0.01)
            except:
                # Handle any error during text typing
                print('Error writing text!')
