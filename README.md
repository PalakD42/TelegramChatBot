# 🤖 TelegramChatBot

An AI-powered Telegram chatbot built with **Python**, **Aiogram**, and **Google Gemini 2.5 Flash**. The bot can answer questions, assist with coding, explain concepts, and engage in natural conversations directly on Telegram.

## ✨ Features

- 🤖 AI-powered conversations using Google Gemini 2.5 Flash
- 💬 Telegram Bot built with Aiogram
- ⚡ In-memory caching for repeated queries
- 🔐 Secure API key management with `.env`
- 🚀 Asynchronous architecture using `asyncio`
- 🛡️ Graceful error handling for API rate limits
- 📱 Easy to set up and deploy

---

## 🛠️ Tech Stack

- Python 3.10+
- Aiogram
- Google Gemini API
- python-dotenv
- Asyncio

---

## 📂 Project Structure

```text
TelegramChatBot/
│── main.py
│── requirements.txt
│── .env
│── .gitignore
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/PalakD42/TelegramChatBot.git
cd TelegramChatBot
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Bot

```bash
python main.py
```

Expected output:

```text
🚀 ShiviiAI Bot is running...
```

---

## 💬 Bot Commands

| Command | Description |
|----------|-------------|
| `/start` | Start the bot |
| `/about` | About the bot |

Send any message to chat with the AI.

---

## ⚙️ How It Works

1. The user sends a message to the Telegram bot.
2. The bot checks whether the query exists in the cache.
3. If found, the cached response is returned instantly.
4. Otherwise, the request is sent to Google Gemini.
5. Gemini generates a response.
6. The response is cached and sent back to the user.

---

## 📦 Dependencies

Install all required packages with:

```bash
pip install -r requirements.txt
```

Main libraries used:

- aiogram
- google-generativeai
- python-dotenv

---

## 🔒 Security

- Store API keys in the `.env` file.
- Do not commit the `.env` file to GitHub.
- Ensure `.env` is included in `.gitignore`.

---

## 🚀 Future Improvements

- 🧠 Conversation history
- 🌍 Multi-language support
- 🎙️ Voice message support
- 📄 PDF and document summarization
- 🖼️ Image analysis
- ☁️ Cloud deployment
- 💾 Database integration
- 📊 Usage analytics

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Palak Dwivedi**

- GitHub: https://github.com/PalakD42
- Telegram Bot: https://t.me/ShiviiAI_bot

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
