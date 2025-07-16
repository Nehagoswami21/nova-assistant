# command.py
import datetime
import webbrowser
import joblib
import os
from user_profile import get_user_profile

model = joblib.load("intent_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


def handle_command(command):
    command = command.lower()

    try:
        X = vectorizer.transform([command])
        prediction = model.predict(X)[0]


        if prediction == "greet":
            return f"Hello! I'm {get_user_profile('assistant_name', 'Nova')}. How can I help you?"

        elif prediction == "tell_time":
            now = datetime.datetime.now().strftime("%I:%M %p")
            return f"The time is {now}"

        elif prediction == "ask_name":
            return f"My name is {get_user_profile('assistant_name', 'Nova')}."

        elif prediction == "ask_creator":
            return f"I was created by {get_user_profile('creator_name', 'Neha Giri Goswami')}."

        elif prediction == "play_music":
            webbrowser.open("https://open.spotify.com/")
            return "Playing some music for you."

        elif prediction == "exit":
            return "Goodbye!"

        elif prediction == "get_weather":
            return "Weather functionality coming soon."

        elif prediction == "ask_my_age":
            return "I'm not sure about your age yet."

        else:
            return "__USE_LLM__"

    except Exception as e:
        print(f"Command error: {e}")
        return "__USE_LLM__"
