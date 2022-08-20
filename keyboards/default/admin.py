from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="📤 Xabar yuborish"),
        KeyboardButton(text="🔋 Ma'lumotlar ombori"),
        ],
        [
        KeyboardButton(text="👤 Foydalanuvchiga xabar yuborish"),
        KeyboardButton(text="📊 Foydalanuvchilar soni"),
        ],
        [
        KeyboardButton(text='👨‍👦‍👦AddUser')
        ]
    ], resize_keyboard=True
)
