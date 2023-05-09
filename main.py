# from dotenv import load_dotenv
from config import dp, scheduler, bot
from aiogram.dispatcher.filters import Text
from aiogram import executor
from handlers.shop import show_catergories, pizza, address, show_hits
import logging
from handlers.survey_fsm import (start_survey,
                                 process_name,
                                 process_age,
                                 process_gender,
                                 inst,
                                 who_is_interested,
                                 Survey)
from scheduler.reminder import start_reminder
from db.base import (
                     DB_PATH,
                     DB_NAME,
                     create_tables,
                     insert_products,
                     insert_survey,
                     db,
                     cursor
                     )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    create_tables()
    DB_NAME
    DB_PATH
    db
    cursor

    scheduler.start()

    dp.register_message_handler(show_catergories, commands=['start'])
    dp.register_message_handler(address, Text(equals="Адресс"))
    dp.register_message_handler(pizza, Text(equals="Пиццы"))
    dp.register_message_handler(show_hits, Text(equals='ХИТЫ'))

    dp.register_message_handler(start_survey, commands=['surv'])
    dp.register_message_handler(process_name, state=Survey.name)
    dp.register_message_handler(process_age, state=Survey.age)
    dp.register_message_handler(inst, state=Survey.inst)
    dp.register_message_handler(process_gender, state=Survey.gender)
    dp.register_message_handler(who_is_interested, state=Survey.who_is_interested)
    executor.start_polling(dp, skip_updates=True)

    dp.register_message_handler(start_reminder, commands=['rem'])
    #dp.register_message_handler(reminder, Text("напомнить"))

