import os
import random
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types


load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('негрррр')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('команды \n'
                         f'/start - запуск бота'
                         f'/help - показать все команды'
                         f'/my_info - информация о вас'
                         f'/pic - рандомная картинка ')


@dp.message_handler(commands=['my_info'])
async def my_info(message: types.Message):
    aid = message.from_user.id
    first_name = message.from_user.first_name
    nickname = message.from_user.username
    await message.answer(f'твой id - {aid}\n'
                         f'твой username - {first_name}'
                         f'твой nickname - {nickname}')


@dp.message_handler(commands=['pic'])
async def pic(message: types.Message):

    images = os.listdir("images")
    image = random.choice(images)
    with open(f"images/{image}", "rb") as f:
        await bot.send_photo(chat_id=message.from_user.id, photo=f)


if __name__ == "__main__":
    executor.start_polling(dp)

