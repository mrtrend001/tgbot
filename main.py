# from dotenv import load_dotenv
from config import dp
from aiogram.dispatcher.filters import Text
from aiogram import executor
from handlers.shop import show_catergories
import logging
from handlers.shop import pizza, address
from handlers.survey_fsm import (start_survey,
                                 process_name,
                                 process_age,
                                 process_gender,
                                 inst,
                                 who_is_interested,
                                 Survey)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)


# load_dotenv()
# bot = Bot(('BOT_TOKEN'))
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
    dp.register_message_handler(show_catergories, commands=['start'])
    dp.register_message_handler(address, Text(equals="Адресс"))
    dp.register_message_handler(pizza, Text(equals="Пиццы"))

    dp.register_message_handler(start_survey, commands=['surv'])
    dp.register_message_handler(process_name, state=Survey.name)
    dp.register_message_handler(process_age, state=Survey.age)
    dp.register_message_handler(inst, state=Survey.inst)
    dp.register_message_handler(process_gender, state=Survey.gender)
    dp.register_message_handler(who_is_interested, state=Survey.who_is_interested)
    executor.start_polling(dp, skip_updates=True)

