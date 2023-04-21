import os
from dotenv import load_dotenv
from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from handlers.shop import show_catergories
import logging
from handlers.shop import pizza, address

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

dp.register_message_handler(show_catergories, commands=['start'])
dp.register_message_handler(address, Text(equals="Адресс"))
dp.register_message_handler(pizza, Text(equals="Пиццы"))

executor.start_polling(dp)
