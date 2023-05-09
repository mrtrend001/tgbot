from aiogram import types
from datetime import datetime
from config import scheduler, bot


#async def start_reminder(message: types.Message):
#    await message.answer('Напишите: "напомнить" + что нужно напомнить')


async def start_reminder(message: types.Message):
    scheduler.add_job(
        send_reminder,
        'interval',
        seconds=11,
        args=(message.from_user.id,)
    )
    await message.answer("Слушаю и повинуюсь!")


async def send_reminder(user_id: int):
    await bot.send_message(
        chat_id=user_id,
        text="Напоминаю, что нужно {}"
    )



