import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден. Добавь его в Railway → Variables")

MINI_APP_URL = "https://crypto-mini-app.vercel.app"  # заменишь на свой URL

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(msg: Message):
    await msg.answer("Привет! Нажми /menu чтобы открыть мини-апку!")

@dp.message(Command("menu"))
async def open_menu(msg: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Открыть мини-апку", web_app=WebAppInfo(url=MINI_APP_URL))
    ]])
    await msg.answer("Открываю мини-апку 👇", reply_markup=kb)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
