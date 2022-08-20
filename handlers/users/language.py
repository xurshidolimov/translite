from keyboards.default.button import main_button_uz, main_button_en, main_button_ru, main_button_tr
from aiogram import types
from loader import dp


@dp.message_handler(text="🇺🇿 o'zbekcha")
async def set_lang_uz(message: types.Message):
    await message.answer("Qaysi lug'atdan foydalanishni xohlaysiz?", reply_markup=main_button_uz)


@dp.message_handler(text="🇬🇧 english")
async def set_lang_en(message: types.Message):
    await message.answer("Which dictionary do you want to use?", reply_markup=main_button_en)


@dp.message_handler(text="🇷🇺 русский")
async def set_lang_ru(message: types.Message):
    await message.answer("Какой словарь вы хотите использовать?", reply_markup=main_button_ru)


@dp.message_handler(text="🇹🇷 türkçe")
async def set_lang_tr(message: types.Message):
    await message.answer("Hangi sözlüğü kullanmak istiyorsun?", reply_markup=main_button_tr)



