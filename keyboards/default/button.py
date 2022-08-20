from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


language_button = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="🇺🇿 o'zbekcha"),
        KeyboardButton(text="🇬🇧 english"),
        ],
        [
        KeyboardButton(text="🇷🇺 русский"),
        KeyboardButton(text="🇹🇷 türkçe"),
        ]
    ], resize_keyboard=True
)

main_button_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="🇺🇿o'zb  ➡️ 🇬🇧ingl"),
        KeyboardButton(text="🇬🇧ingl  ➡️ 🇺🇿o'zb"),
        ],
        [
        KeyboardButton(text="🇺🇿o'zb  ➡️ 🇷🇺rus"),
        KeyboardButton(text="🇷🇺rus  ➡️ 🇺🇿o'zb"),
        ],
        [
        KeyboardButton(text="🇺🇿o'zb  ➡️ 🇹🇷turk"),
        KeyboardButton(text="🇹🇷turk  ➡️ 🇺🇿o'zb"),
        ]
    ], resize_keyboard=True
)

main_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="🇷🇺рус  ➡️ 🇬🇧анг"),
        KeyboardButton(text="🇬🇧анг  ➡️ 🇷🇺рус"),
        ],
        [
        KeyboardButton(text="🇷🇺рус  ➡️ 🇺🇿узб"),
        KeyboardButton(text="🇺🇿узб  ➡️ 🇷🇺рус"),
        ],
        [
        KeyboardButton(text="🇷🇺рус  ➡️ 🇹🇷тур"),
        KeyboardButton(text="🇹🇷тур  ➡️ 🇷🇺рус"),
        ]
    ], resize_keyboard=True
)

main_button_en = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="🇬🇧eng  ➡️ 🇺🇿uzb"),
        KeyboardButton(text="🇺🇿uzb  ➡️ 🇬🇧eng"),
        ],
        [
        KeyboardButton(text="🇬🇧eng  ➡️ 🇷🇺rus"),
        KeyboardButton(text="🇷🇺rus  ➡️ 🇬🇧eng"),
        ],
        [
        KeyboardButton(text="🇬🇧eng  ➡️ 🇹🇷turc"),
        KeyboardButton(text="🇹🇷turc  ➡️ 🇬🇧eng"),
        ]
    ], resize_keyboard=True
)

main_button_tr = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="🇹🇷Türk  ➡️ 🇬🇧İng"),
        KeyboardButton(text="🇬🇧İng  ➡️ 🇹🇷Türk"),
        ],
        [
        KeyboardButton(text="🇹🇷Türk  ➡️ 🇷🇺Rus"),
        KeyboardButton(text="🇷🇺Rus  ➡️ 🇹🇷Türk"),
        ],
        [
        KeyboardButton(text="🇹🇷Türk  ➡️ 🇺🇿Özb"),
        KeyboardButton(text="🇺🇿Özb  ➡️ 🇹🇷Türk"),
        ]
    ], resize_keyboard=True
)