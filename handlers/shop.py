from aiogram import types


kb = types.ReplyKeyboardMarkup()


async def show_catergories(message: types.Message):
    kb.add(types.KeyboardButton("Пиццы"))
    kb.add(types.KeyboardButton("Адрес"))
    await message.answer(
        f"Выберите категорию",
        reply_markup=kb
    )


async def address(message: types.Message):
    await message.answer("ГДЕ-ТО")


async def pizza(message: types.Message):
    kb.add(types.KeyboardButton("Сицилийская пицца (Pizza Siciliana)"))
    kb.add(types.KeyboardButton("Метровая пицца (Pizza al metro или Pizza alla Palla)"))
    kb.add(types.KeyboardButton("Римская пицца (Pizza Romana)"))
    kb.add(types.KeyboardButton("Пицца в нарезке (Pizza al taglio)"))
    await message.answer(
        f"Меню",
        reply_markup=kb
    )
