from aiogram import types
from loader import dp, db


@dp.message_handler(text="🇷🇺рус  ➡️ 🇬🇧анг")
async def set_languz_uzen(message: types.Message):
    try:
        db.update_user_lang(lang1='ru', lang2='en', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇬🇧анг  ➡️ 🇷🇺рус")
async def set_languz_enuz(message: types.Message):
    try:
        db.update_user_lang(lang1='en', lang2='ru', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇷🇺рус  ➡️ 🇺🇿узб")
async def set_languz_uzru(message: types.Message):
    try:
        db.update_user_lang(lang1='ru', lang2='uz', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇺🇿узб  ➡️ 🇷🇺рус")
async def set_languz_ru(message: types.Message):
    try:
        db.update_user_lang(lang1='uz', lang2='ru', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇷🇺рус  ➡️ 🇹🇷тур")
async def set_languz_uztr(message: types.Message):
    try:
        db.update_user_lang(lang1='ru', lang2='tr', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass

@dp.message_handler(text="🇹🇷тур  ➡️ 🇷🇺рус")
async def set_languz_truz(message: types.Message):
    try:
        db.update_user_lang(lang1='tr', lang2='ru', id=message.from_user.id)
        await message.answer("ok")
    except:
        pass
