from aiogram import types
from loader import dp, db


@dp.message_handler(text="🇺🇿o'zb  ➡️ 🇬🇧ingl")
async def set_languz_uzen(message: types.Message):
    try:
        db.update_user_lang(lang1='uz', lang2='en', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇬🇧ingl  ➡️ 🇺🇿o'zb")
async def set_languz_enuz(message: types.Message):
    try:
        db.update_user_lang(lang1='en', lang2='uz', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇺🇿o'zb  ➡️ 🇷🇺rus")
async def set_languz_uzru(message: types.Message):
    try:
        db.update_user_lang(lang1='uz', lang2='ru', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇷🇺rus  ➡️ 🇺🇿o'zb")
async def set_languz_ru(message: types.Message):
    try:
        db.update_user_lang(lang1='ru', lang2='uz', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇺🇿o'zb  ➡️ 🇹🇷turk")
async def set_languz_uztr(message: types.Message):
    try:
        db.update_user_lang(lang1='uz', lang2='tr', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇹🇷turk  ➡️ 🇺🇿o'zb")
async def set_languz_truz(message: types.Message):
    try:
        db.update_user_lang(lang1='tr', lang2='uz', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass