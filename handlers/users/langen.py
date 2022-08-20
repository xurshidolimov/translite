from aiogram import types
from loader import dp, db


@dp.message_handler(text="🇬🇧eng  ➡️ 🇺🇿uzb")
async def set_languz_uzen(message: types.Message):
    try:
        db.update_user_lang(lang1='en', lang2='uz', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇺🇿uzb  ➡️ 🇬🇧eng")
async def set_languz_enuz(message: types.Message):
    try:
        db.update_user_lang(lang1='uz', lang2='en', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇬🇧eng  ➡️ 🇷🇺rus")
async def set_languz_uzru(message: types.Message):
    try:
        db.update_user_lang(lang1='en', lang2='ru', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇷🇺rus  ➡️ 🇬🇧eng")
async def set_languz_ru(message: types.Message):
    try:
        db.update_user_lang(lang1='ru', lang2='en', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇬🇧eng  ➡️ 🇹🇷turc")
async def set_languz_uztr(message: types.Message):
    try:
        db.update_user_lang(lang1='en', lang2='tr', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇹🇷turc  ➡️ 🇬🇧eng")
async def set_languz_truz(message: types.Message):
    try:
        db.update_user_lang(lang1='tr', lang2='en', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass
