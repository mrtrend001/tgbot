from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler


load_dotenv()
bot = Bot(getenv('BOT_TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
scheduler = AsyncIOScheduler()
