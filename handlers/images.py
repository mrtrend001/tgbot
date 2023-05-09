import os
import random
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types


async def pic(message: types.Message):
    images = os.listdir("images")
    image = random.choice(images)
    with open(f"images/{image}", "rb") as f:
        await Bot.send_photo(chat_id=message.from_user.id, photo=f)

