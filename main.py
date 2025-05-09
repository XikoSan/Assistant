import json, os
from llama3 import ask_llama
from history_module import build_chat_history, chat_history

HISTORY_PATH = "history.json"

# — Загрузка истории
if os.path.exists(HISTORY_PATH):
    try:
        with open(HISTORY_PATH, "r") as f:
            chat_history = json.load(f)
    except json.JSONDecodeError:
        chat_history = []
else:
    chat_history = []

# — Запрос
if __name__ == "__main__":
    user_msg = input("You: ")
    chat_history.append({"role": "user", "content": user_msg})

    prompt = build_chat_history(chat_history) + "\nAssistant:"
    answer = ask_llama(prompt)
    print(answer)

    chat_history.append({"role": "assistant", "content": answer})

    # — Сохранение
    with open(HISTORY_PATH, "w", encoding="utf-8") as f:
        json.dump(chat_history, f, ensure_ascii=False, indent=2)

