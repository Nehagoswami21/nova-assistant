# recognizer.py

import sounddevice as sd
import numpy as np
import whisper
import scipy.io.wavfile
import os


model = whisper.load_model("base")  # You can use "tiny" for faster response

def listen_and_recognize():
    duration = 6  # seconds
    fs = 16000

    print("🎤 Listening for 6 seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()

    audio = np.squeeze(audio)
    scipy.io.wavfile.write("temp.wav", fs, (audio * 32767).astype(np.int16))

    print("🧠 Transcribing...")
    os.environ["PATH"] += os.pathsep + r"C:\Users\rishi\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin"
    result = model.transcribe("temp.wav")
    text = result["text"].strip()

    print(f"🗣 You said: {text}")
    return text