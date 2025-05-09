import requests

def ask_llama(prompt:str) -> str:

    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
        }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=data)

        result = response.json()
        return result["response"]
    except Exception:
        return "Ошибка соединения"
