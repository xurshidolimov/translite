import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.button import language_button
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    await message.answer(f"Hello {name}!!!", reply_markup=language_button)

    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id, lang1='uz', lang2='en', name=name)
    except sqlite3.IntegrityError as err:
        pass