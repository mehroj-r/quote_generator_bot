import logging

from aiogram import Bot, Dispatcher, executor, types
from functions import getRandomQuote
from aiogram.types import ParseMode

API_TOKEN = 'BOT_TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Hi, {message.from_user.full_name} ! Welcome to <b>Motivational Quotes Bot</b>. \n\nSend /help to learn how to get started.", parse_mode = ParseMode.HTML)

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("• <b>Options in Motivational Quotes Bot</b>: \n\n /quote - To get random quote ", parse_mode = ParseMode.HTML)

@dp.message_handler(commands=['quote'])
async def send_welcome(message: types.Message):

    response = getRandomQuote()
    await message.answer(response, parse_mode = ParseMode.HTML)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)