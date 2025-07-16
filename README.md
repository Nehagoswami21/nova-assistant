# Nova Assistant 🤖

Nova is a locally-running voice assistant built with Python, Whisper for speech recognition, and a custom-trained intent classifier. It can greet you, tell the time, play music, and even answer questions — all privately and offline.

---

## 🛠 Features

- 🎤 Speech recognition using OpenAI Whisper
- 🧠 Custom command intent detection
- 🔊 Offline speech via `pyttsx3`
- ⏱ Tells time
- 🎵 Opens Spotify
- 🌦️ Weather queries (planned)
- 🧠 Fallback to LLM for general questions

---

## Getting Started

```bash
git clone https://github.com/Nehagoswami21/nova-assistant.git
cd nova-assistant
pip install -r requirements.txt
python main.py

## 🗣 How to Use
Once Nova starts, it will listen for your voice and try to recognize commands such as:

"hello" — Greeting

"what time is it" — Tells the current time

"play music" — Opens Spotify in your browser

"what's your name" — Replies with its name

"who created you" — Tells about its creator

"goodbye" — Exits the assistant

Talk naturally, and wait for Nova to respond. It listens for 6 seconds by default per input.

##  Requirements
Make sure you have the following installed:

Python 3.8+

FFmpeg (required by Whisper)
👉 Download FFmpeg and ensure it's added to your system PATH

Install dependencies again (if needed):
pip install -r requirements.txt
---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! If you’d like to help improve Nova Assistant:

1. **Fork** the repository
2. **Create a branch** (`git checkout -b feature/your-feature`)
3. **Commit your changes** (`git commit -m 'Add some feature'`)
4. **Push to the branch** (`git push origin feature/your-feature`)
5. **Open a Pull Request**

Please make sure to follow clear coding practices and include helpful commit messages.
---

## Licensed
This project is licensed under the MIT License.
You’re free to use, modify, and share Nova under the terms of this license.



