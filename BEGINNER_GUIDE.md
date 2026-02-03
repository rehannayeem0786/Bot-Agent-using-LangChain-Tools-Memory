# 🎓 Beginner's Guide - Understand the Code

## 📄 Main Files Explained

### `simple_chat.py` - The Bot

The core chat loop:
```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

while True:
    user_input = input("You: ")
    if user_input == "exit": break
    response = llm.invoke(user_input)
    print(f"Bot: {response.content}")
```

### `config.py` - Configuration

Loads your API key from `.env`:
```python
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

### `.env` - Credentials

Store your secret API key:
```
OPENAI_API_KEY=sk-or-v1-your-key-here
```

## 💡 Key Concepts

**🧠 LLM (Language Model)**
- The AI that understands and responds
- We use OpenAI's GPT-3.5-Turbo via Open Router

**💾 Memory/Context**
- Bot remembers past messages
- Sends full history to AI for context

**🔑 API Key**
- Secret code to use the AI service
- Never share it!
- Get free: https://openrouter.ai

## 🔧 Modify & Extend

**Change bot personality:**
```python
system_prompt = "You are a funny comedian"
```

**Save conversations to file:**
```python
with open("chats.txt", "a") as f:
    f.write(f"User: {user}\nBot: {response}\n\n")
```

**Add a tool (function the AI can call):**
```python
from langchain.tools import tool

@tool
def search_web(query: str) -> str:
    """Search the internet"""
    return results
```

## ❓ Common Questions

**Q: How does the bot remember?**
A: We keep all past messages and send them with each new request to the AI.

**Q: Can I change how the bot talks?**
A: Yes! Modify the system prompt to change its personality.

**Q: How do I save chats?**
A: Write each message to a text file after the bot responds.

## 📖 Learning Path

1. ✅ Run `python simple_chat.py`
2. ✅ Chat with the bot
3. ✅ Modify the system prompt
4. ✅ Add logging to file
5. ✅ Explore adding new features

---

**Next:** Try the bot, then read `TUTORIAL.md`
