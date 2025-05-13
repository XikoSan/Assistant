# Assistant

Экспериментальный проект — персональный AI-ассистент на базе локально запущенной LLaMA 3 и Python-стека.

## 🧠 Стек

| Слой            | Технология                   | Почему                                   |
|-----------------|-----------------------------|------------------------------------------|
| LLM             | **LLaMA 3** через **Ollama**| Бесплатно, локально, без облачных ключей |
| Backend-HTTP    | **FastAPI + Uvicorn**       | Роуты `/ping`, `/chat`, авто-Swagger     |
| Клиент к LLM    | `requests`                  | POST-вызовы в Ollama API                 |
| CLI             | `main.py`                   | Интерактивный чат из терминала           |
| Memory          | `history.json`              | Контекст между запусками                 |
| Roadmap         | LangChain, векторное хранилище, CORS-фронтенд |

## 🚀 Быстрый старт

```bash
# 1. Клонируем репозиторий
git clone git@github.com:<user>/assistant.git
cd assistant

# 2. Ставим Ollama и модель
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3

# 3. Устанавливаем зависимости
pip install -r requirements.txt   # fastapi, uvicorn, pydantic, requests

# 4. Запускаем веб-сервер
uvicorn api:app --reload --port 8000   # Swagger на /docs

# 5. (опция) CLI-чат
python main.py

assistant/
 ├─ api.py             # FastAPI-сервер (/ping, /chat)
 ├─ llama3.py          # ask_llama(): обёртка Ollama API
 ├─ history_module.py  # chat_history + build_chat_history()
 ├─ main.py            # CLI-чат + загрузка/сохранение памяти
 ├─ history.json       # долговременная память (автогенерируется)
 └─ requirements.txt
