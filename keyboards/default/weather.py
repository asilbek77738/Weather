from  aiogram.types import KeyboardButton, ReplyKeyboardMarkup

WeatherUZ = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Bugungi ob-havo")],
        [KeyboardButton(text="🗓 3 kunga ma'lumot")],
        [KeyboardButton(text="⚙️ Sozlamalar")]
    ],
    resize_keyboard=True
)
WeatherRU = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Прогноз на сегодня")],
        [KeyboardButton(text="🗓 Прогноз на 3 дня")],
        [KeyboardButton(text="⚙️ Настройки")]
    ],
    resize_keyboard=True
)