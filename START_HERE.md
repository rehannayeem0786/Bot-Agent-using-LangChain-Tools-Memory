# 🚀 Start Here - 2 Minute Setup

## 1️⃣ Install Dependencies
```powershell
pip install -r requirements.txt
```

## 2️⃣ Configure API Key
Edit **`.env`** and add:
```
OPENAI_API_KEY=sk-or-v1-your-api-key-here
```

> 💡 **Get a free API key:** https://openrouter.ai

## 3️⃣ Run the Bot

```powershell
cd C:\Users\91984\Task\conversational-knowledge-bot
python simple_chat.py
```

That's it! Start chatting! 💬

## ❓ Quick Fixes

**Bot doesn't respond?**
- ✓ Check `.env` has your API key
- ✓ Check internet connection

**`ModuleNotFoundError`?**
- ✓ Run: `pip install -r requirements.txt`

**`API key error`?**
- ✓ Verify `.env` key starts with `sk-or-v1-`

## 📁 Key Files

```
simple_chat.py  ← Run this
config.py       ← Loads API key
.env            ← Your credentials
requirements.txt ← Dependencies
```

---

**Next:** Read `BEGINNER_GUIDE.md` to understand the code
