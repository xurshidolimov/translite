from aiogram import types
from loader import dp, db


@dp.message_handler(text="🇹🇷Türk  ➡️ 🇬🇧İng")
async def set_languz_uzen(message: types.Message):
    db.update_user_lang(lang1='tr', lang2='en', id=message.from_user.id)
    await message.answer("ok")


@dp.message_handler(text="🇬🇧İng  ➡️ 🇹🇷Türk")
async def set_languz_enuz(message: types.Message):
    db.update_user_lang(lang1='en', lang2='tr', id=message.from_user.id)
    await message.answer("ok")


@dp.message_handler(text="🇹🇷Türk  ➡️ 🇷🇺Rus")
async def set_languz_uzru(message: types.Message):
    db.update_user_lang(lang1='tr', lang2='ru', id=message.from_user.id)
    await message.answer("ok")


@dp.message_handler(text="🇷🇺Rus  ➡️ 🇹🇷Türk")
async def set_languz_ru(message: types.Message):
    db.update_user_lang(lang1='ru', lang2='tr', id=message.from_user.id)
    await message.answer("ok")

@dp.message_handler(text="🇹🇷Türk  ➡️ 🇺🇿Özb")
async def set_languz_uztr(message: types.Message):
    db.update_user_lang(lang1='tr', lang2='uz', id=message.from_user.id)
    await message.answer("ok")


@dp.message_handler(text="🇺🇿Özb  ➡️ 🇹🇷Türk")
async def set_languz_truz(message: types.Message):
    db.update_user_lang(lang1='uz', lang2='tr', id=message.from_user.id)
    await message.answer("ok")

