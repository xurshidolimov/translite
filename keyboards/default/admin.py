from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="π€ Xabar yuborish"),
        KeyboardButton(text="π Ma'lumotlar ombori"),
        ],
        [
        KeyboardButton(text="π€ Foydalanuvchiga xabar yuborish"),
        KeyboardButton(text="π Foydalanuvchilar soni"),
        ],
        [
        KeyboardButton(text='π¨βπ¦βπ¦AddUser')
        ]
    ], resize_keyboard=True
)
