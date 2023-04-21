import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types


async def my_info(message: types.Message):
    aid = message.from_user.id
    first_name = message.from_user.first_name
    nickname = message.from_user.username
    await message.answer(f'твой id - {aid}\n'
                         f'твой username - {first_name}'
                         f'твой nickname - {nickname}')


async def help(message: types.Message):
    await message.answer('команды \n'
                         f'/start - запуск бота'
                         f'/help - показать все команды'
                         f'/my_info - информация о вас'
                         f'/pic - рандомная картинка ')
