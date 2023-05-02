from aiogram import types
from config import bot, scheduler


async def start_reminder(message: types.Message):
    scheduler.add_job(
        send_reminder,
        'interval',
        seconds=5,
        args=(message.from_user.id,)
    )
    await message.answer("Слушаю и повинуюсь!")


async def send_reminder(user_id: int):
    await bot.send_message(
        chat_id=user_id,
        text="Напоминаю"
    )