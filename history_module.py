chat_history = [
   
]

def build_chat_history(history) -> str:

    lines = []

    for entry in history:
        if entry["role"] == "user":
            lines.append("You: " + entry["content"])
        elif entry["role"] == "assistant":
            lines.append("Assistant: " + entry["content"])

    return "\n".join(lines)

print(build_chat_history(chat_history))
