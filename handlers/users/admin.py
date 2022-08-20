import asyncio
import sqlite3

from aiogram.dispatcher import FSMContext
from aiogram import types
from data.config import ADMINS
from keyboards.default.admin import admin
from loader import dp, db, bot
from states.states import SendMessage, SendReklama, AddUser


@dp.message_handler(commands=['admin'], user_id=ADMINS)
async def send_welcome(message: types.Message):
    try:
        if message.from_user.id in ADMINS or message.from_user.id == 679932311:
            await message.reply(f"Salom Translate telegram boti admin paneliga xush kelibsiz!", reply_markup=admin)
    except:
        pass


@dp.message_handler(text="🔋 Ma'lumotlar ombori", user_id=ADMINS)
async def get_all_users(message: types.Message):
    try:
        users = db.select_all_users()
        await message.answer(users)
    except:
        pass

@dp.message_handler(text="📊 Foydalanuvchilar soni", user_id=ADMINS)
async def count(message: types.Message):
    try:
        await message.answer(db.count_users())
    except:
        pass

@dp.message_handler(text="👤 Foydalanuvchiga xabar yuborish", user_id=ADMINS, state=None)
async def send_message_user_1(message: types.Message):
    try:
        await message.answer("Foydalanuvchi 'id'sini kiriting")
        await SendMessage.id.set()
    except:
        pass

@dp.message_handler(state=SendMessage.id)
async def send_message_user_2(message: types.Message, state: FSMContext):
    try:
        id = message.text
        await state.update_data({'id': id})
        await message.answer("Xabarni kiriting")
        await SendMessage.next()
    except:
        pass

@dp.message_handler(state=SendMessage.xabar)
async def send_message_user_3(message: types.Message, state: FSMContext):
    try:
        xabar = message.text
        await state.update_data({'xabar': xabar})

        # foydalanuvchiga yuborish
        data = await state.get_data()
        id = data['id']
        mess = data['xabar']
        await bot.send_message(chat_id=id, text=mess)

        # adminga hisobot berish
        await message.answer("Xabar yuborildi")
        await state.finish()
    except:
        pass

@dp.message_handler(text="📤 Xabar yuborish", user_id=ADMINS)
async def send_reklama(message:types.Message):
    try:
        await message.answer("Reklama yuborish uchun /pwerklsdmamdmca5sds58d3s comandasini kiriting")
    except:
        pass

@dp.message_handler(commands=['pwerklsdmamdmca5sds58d3s'], user_id=ADMINS, state=None)
async def send_message_all_user_1(message: types.Message):
    try:
        await message.answer("Xabar matnini kiriting")
        await SendReklama.rek.set()
    except:
        pass

@dp.message_handler(state=SendReklama.rek)
async def send_message_all_users_2(message: types.Message, state: FSMContext):
    try:
        rek = message.text
        await state.update_data({'rek': rek})

        # foydalanuvchilarga xabar yuborish
        data = await state.get_data()
        xat = data['rek']
        users = db.select_all_users()
        for user in users:
            user_id = user[0]
            await bot.send_message(chat_id=user_id, text=xat)
            await asyncio.sleep(0.05)

        # adminga hisobot berish
        await message.answer("Xabar yuborildi")
        await state.finish()
    except:
        pass

# new
@dp.message_handler(text="👨‍👦‍👦AddUser", user_id=ADMINS, state=None)
async def add_user1(message: types.Message):
    try:
        await message.answer("Foydalanuvchi 'id'sini kiriting")
        await AddUser.id.set()
    except:
        pass


@dp.message_handler(state=AddUser.id)
async def add_user2(message: types.Message, state: FSMContext):
    try:
        id = message.text
        await state.update_data({'id': id})
        await message.answer("Ismini kiriting")
        await AddUser.next()
    except:
        pass

@dp.message_handler(state=AddUser.name)
async def send_message_user_3(message: types.Message, state: FSMContext):
    try:
        name = message.text
        await state.update_data({'name': name})

        # create user
        data = await state.get_data()
        id = data['id']
        name = data['name']

        try:
            db.add_user(id=id, lang1='uz', lang2='en', name=name)
        except sqlite3.IntegrityError as err:
            pass

        # adminga hisobot berish
        await message.answer("Foydalanuvchi saqlandi")
        await state.finish()
    except:
        pass