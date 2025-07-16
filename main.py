from recognizer import listen_and_recognize
from ollama_handler import get_llm_response
from commands import handle_command
from speaker import speak
import config

def main():
    print(f"🟡 {config.assistant_name} is running. Say something...")

    while True:
        command = listen_and_recognize()

        if not command:
            print("⚠️ Didn't catch that. Try again.\n")
            continue

        if "exit" in command.lower() or "quit" in command.lower():
            print("👋 Exiting. Goodbye!")
            speak("Goodbye!")
            break

        result = handle_command(command)
        response = get_llm_response(command) if result == "__USE_LLM__" else result

        print(f"🤖 {config.assistant_name}: {response}\n")
        speak(response)

if __name__ == "__main__":
    main()
