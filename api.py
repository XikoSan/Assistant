from fastapi import FastAPI
from pydantic import BaseModel
from llama3 import ask_llama
from history_module import build_chat_history, chat_history

app = FastAPI(title="AI Assistant")

@app.get("/ping")
def ping():
    return {"pong": True}

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    answer: str

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    chat_history.append({"role": "user", "content": req.message})

    prompt = build_chat_history(chat_history) + "\nAssistant:"
    answer = ask_llama(prompt)

    chat_history.append({"role": "assistant", "content": answer})
    return ChatResponse(answer=answer)

