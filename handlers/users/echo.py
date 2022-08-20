import sqlite3

from aiogram import types
from deep_translator import GoogleTranslator
from loader import dp, db



# translate
@dp.message_handler(state=None)
async def echo(message: types.Message):
    user = list(db.select_user(id=message.from_user.id))
    lang1 = user[2]
    lang2 = user[3]

    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id, lang1=lang1, lang2=lang2, name=message.from_user.full_name)
    except sqlite3.IntegrityError as err:
        pass


    await message.answer(GoogleTranslator(source=lang1, target=lang2).translate(message.text))

