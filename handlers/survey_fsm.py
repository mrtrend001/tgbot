from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from db.base import insert_survey


class Survey(StatesGroup):
    name = State()
    age = State()
    gender = State()
    inst = State()
    who_is_interested = State()


async def start_survey(message: types.Message):
    await Survey.name.set()

    await message.answer("Ваше имя")


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        print(data)

    await Survey.next()
    await message.answer("Сколько вам лет?")


async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer('введите цифры')
    elif int(age) > 200 or int(age) < 6:
        await message.answer("Введенный возраст не обслужывается")
    else:
        async with state.proxy() as data:
            data['age'] = int(age)
            print(data)

    await Survey.next()

    kb = types.ReplyKeyboardMarkup()
    kb.add("Мужской", "Женский")
    await message.answer("Ваш пол?", reply_markup=kb)


async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

    print(data, message.text, message.from_user.id)
    await Survey.next()
    await message.answer("Ваш инстаграм")


async def inst(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['inst'] = message.text
        print(data)

    await Survey.next()

    kb = types.ReplyKeyboardMarkup()
    kb.add("Мужчины", "Женшины")
    await message.answer("Кто вас интерисует?", reply_markup=kb)


async def who_is_interested(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['who_is_interested'] = message.text
        insert_survey(data)

    print(data, message.text, message.from_user.id)
    await message.answer("Спасибо за ваше время, которое вы уделили нам")
    await state.finish()


