# llama3_api.py
import requests

def ask_ollama(prompt, model="llama3"):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False    # 💥 Bu satır olmazsa JSONDecodeError alırsın
            }
        )
        response.raise_for_status()
        data = response.json()

        if "response" not in data or not data["response"].strip():
            return "❗ LLM boş yanıt verdi. Lütfen daha açıklayıcı prompt deneyin."

        return data["response"]

    except Exception as e:
        return f"❌ LLM Hatası: {str(e)}"
