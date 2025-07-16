# speaker.py
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)  # Optional: set speech rate
    engine.setProperty('voice', engine.getProperty('voices')[0].id)  # 0 = male, 1 = female (on most systems)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
