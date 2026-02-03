# 📋 Quick Reference Guide

## 🐍 Python Files

**`simple_chat.py`** ⭐ Main chatbot
- Simple chat loop (~120 lines)
- Runs: `python simple_chat.py`
- Contains: Chat UI, memory, API calls

**`config.py`** - Configuration loader
- Reads `.env` file
- Exports: `OPENAI_API_KEY`

## ⚙️ Configuration Files

**`.env`** - Your credentials
```
OPENAI_API_KEY=sk-or-v1-your-key-here
```

**`requirements.txt`** - Dependencies
```
langchain
langchain-openai
python-dotenv
requests
```

## 📚 Documentation

| File | Purpose | Time |
|------|---------|------|
| START_HERE.md | Quick setup | 2 min |
| BEGINNER_GUIDE.md | Learn code | 10 min |
| TUTORIAL.md | Deep dive | 30 min |
| README.md | Overview | 3 min |

## ⚡ Commands

```powershell
# Install packages (run once)
pip install -r requirements.txt

# Go to project folder
cd C:\Users\91984\Task\conversational-knowledge-bot

# Run bot
python simple_chat.py

# Exit bot (in chat)
type: exit
```

## 🔑 Core Code Pattern

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

while True:
    user = input("You: ")
    if user == "exit": break
    response = llm.invoke(user)
    print(f"Bot: {response.content}")
```

## ✅ Setup Checklist

- [ ] Edit `.env` with API key
- [ ] Run `pip install -r requirements.txt`
- [ ] Run `python simple_chat.py`
- [ ] Type something and chat!

---

**Stuck?** Check troubleshooting in START_HERE.md
