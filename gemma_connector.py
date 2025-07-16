# gemma_connector.py
import requests

def query_gemma(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "gemma", "prompt": prompt, "stream": False},
            timeout=15
        )
        data = response.json()
        return data.get("response", "").strip()
    except Exception as e:
        return f"Sorry, I couldn't reach Gemma. Error: {str(e)}"