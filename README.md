## Voice Typing Tool with Python
This project allows you to perform voice typing using Python, the keyboard library, SpeechRecognition, and Whisper from OpenAI.

**Dependencies:**

* keyboard
* SpeechRecognition
* openai-whisper

**Requirements:**

* Python 3.x
* Microphone
* ffmpeg (for Whisper)

**How it works:**

1. **Continuous listening:** The program constantly waits for the user to press the Ctrl+Space keys.
2. **Speech recognition:** When the keys are pressed, it listens to the microphone for 2 seconds and tries to recognize the spoken words.
3. **Audio recording:** If speech is detected, the recognized audio is saved as a WAV file.
4. **Transcription:** The WAV file is transcribed using the Whisper model provided.
5. **Text typing:** If transcription is successful, the recognized text is typed character by character with a slight delay.

**Instructions:**

1. Install the required dependencies: `pip install keyboard SpeechRecognition openai-whisper`
2. Install ffmpeg: Follow the instructions for your platform (https://ffmpeg.org/download.html).
3. Select the Whisper model to download automatically. The default is "base.en".
5. Run the script: `python voice_typing.py`
6. Press and release the Ctrl+Space keys to start recording. Recording will automatically stop when no speech is detected for 1 second.

**How to use Whisper with CUDA**

1. Uninstall PyTorch using the command: `pip uninstall torch torchaudio torchvision`
2. Go to the PyTorch website: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)
3. Select the installation option with CUDA support.
4. Follow the on-screen instructions to install PyTorch.

**Notes:**

* Adjust the `delay` value in the `keyboard.write` function if the typing causes performance issues.

**Contributing:**

Feel free to fork this project and contribute improvements or new features! Pull requests are welcome.
