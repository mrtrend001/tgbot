from aiogram import types
from db.base import get_products


async def show_catergories(message: types.Message):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton("Пиццы"))
    kb.add(types.KeyboardButton("Адрес"))
    await message.answer(
        f"Выберите категорию",
        reply_markup=kb
    )


async def address(message: types.Message):
    await message.answer("ГДЕ-ТО")


async def pizza(message: types.Message):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton("ХИТЫ"))
    kb.add(types.KeyboardButton("Сицилийская пицца (Pizza Siciliana)"))
    kb.add(types.KeyboardButton("Метровая пицца (Pizza al metro или Pizza alla Palla)"))
    kb.add(types.KeyboardButton("Римская пицца (Pizza Romana)"))
    kb.add(types.KeyboardButton("Пицца в нарезке (Pizza al taglio)"))
    await message.answer(
        f"Меню",
        reply_markup=kb
    )


async def show_hits(message: types.Message):

    await message.reply(
        "ХИТЫ недели",
        reply_markup=types.ReplyKeyboardRemove()
    )
    for pr in get_products():
        with open(pr[3], 'rb') as product_pic:
            await message.answer_photo(
                product_pic,
                caption=f"Товар: {pr[1]} по цене {pr[2]}")

