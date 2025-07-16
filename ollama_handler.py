import requests

def get_llm_response(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma:2b",  # ✅ exact match
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"⚠️ Error talking to Gemma: {e}"