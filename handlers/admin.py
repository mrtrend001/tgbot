from aiogram import types


async def example(message: types.Message):
    chat_type = message.chat.type
    reply = message.reply_to_message
    member_type = await message.chat.get_member(
        message.from_user.id
    )
    member_type = member_type['status']
    await message.answer(f"{chat_type=}, {reply=}, {member_type=}")
    if message.chat.type != 'private':
        pass
    if message.reply_to_message:
        pass
