import asyncio
import os

import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ChatAction
from aiogram.filters import Command
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Simple cache
cache = {}

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        """🤖 Welcome to ShiviiAI!

I'm your personal AI assistant powered by Google Gemini.

✨ I can help with:
• Programming & Debugging 💻
• Math & Science 📚
• Writing & Grammar ✍️
• General Knowledge 🌍
• Brainstorming Ideas 💡

Simply send me a message and I'll do my best to help.

Let's get started! 🚀"""
    )


@dp.message(Command("about"))
async def about(message: types.Message):
    await message.answer(
        """🤖 ShiviiAI

Powered by Google Gemini 2.5 Flash

Built with:
🐍 Python
⚡ Aiogram

Version: 1.0"""
    )


@dp.message()
async def ai_chat(message: types.Message):
    try:
        user_text = message.text.strip()

        # Ignore empty messages
        if not user_text:
            return

        # Return cached response if available
        if user_text in cache:
            await message.answer(cache[user_text])
            return

        # Show "typing..."
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        prompt = f"""
You are ShiviiAI, a friendly AI assistant.

Rules:
- Be helpful.
- Be accurate.
- Keep responses clear and concise.
- Use Markdown when appropriate.
- If you don't know something, admit it honestly.

User:
{user_text}
"""

        response = model.generate_content(prompt)
        reply = response.text

        # Save in cache
        cache[user_text] = reply

        await message.answer(reply)

    except Exception as e:
        error = str(e)

        if "429" in error:
            await message.answer(
                "⏳ Gemini API quota exceeded.\nPlease wait a moment and try again."
            )
        else:
            await message.answer(
                f"❌ Something went wrong.\n\n{error}"
            )

async def main():
    print("🚀 ShiviiAI Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())