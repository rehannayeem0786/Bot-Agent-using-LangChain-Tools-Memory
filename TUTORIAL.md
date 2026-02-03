# 📚 Project Tutorial & Essentials

## 🎯 What This Project Does

Builds a conversational AI chatbot that:
- 💬 Chats naturally with users
- 🧠 Remembers conversation context
- ⚙️ Uses LangChain + OpenAI API
- 🚀 Runs locally on your computer

## 📁 Core Files

| File | Purpose |
|------|----------|
| `simple_chat.py` | Main bot program (~120 lines) |
| `config.py` | Loads API configuration |
| `.env` | Stores your API credentials |
| `requirements.txt` | Lists Python packages |

## ⚡ Quick Setup

```powershell
pip install -r requirements.txt
```

**Edit `.env`:**
```
OPENAI_API_KEY=sk-or-v1-your-key-here
```

**Run:**
```powershell
python simple_chat.py
```

## 🔑 How It Works (Core Code)

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

## 🛠️ Customize It

**Change bot personality:**
```python
system_prompt = "You are a helpful Python expert"
```

**Save conversations:**
```python
with open("chat.txt", "a") as f:
    f.write(f"You: {user}\n")
    f.write(f"Bot: {response}\n\n")
```

**Add new features:**
- Web interface (Flask/FastAPI)
- Database storage
- Web search integration

## ❓ Common Issues

| Problem | Solution |
|---------|----------|
| No response | Check API key, internet |
| Module error | `pip install -r requirements.txt` |
| API error | Verify `sk-or-v1-` prefix |

---

**Next:** Explore `BEGINNER_GUIDE.md` for deeper learning
