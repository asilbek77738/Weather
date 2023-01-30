import sqlite3
from aiogram import types
from  keyboards.default.City import cityuz,cityru
from keyboards.default.weather import WeatherRU,WeatherUZ
from . siteWeather import *
from loader import dp,db

@dp.message_handler(text="🗓 3 kunga ma'lumot")
async def bot_echo(message: types.Message):
    try:
        db.add_lang(id=message.from_user.id,
                    )
    except sqlite3.IntegrityError as err:
        pass
    id =message.chat.id
    lang = db.select_lang(id=id)
    if lang[2] == 'NO':
        await message.answer("<b>Iltimos Avval Viloyatni sozlang...</b>",reply_markup=cityuz)
        if lang[2] == 'Toshkent':
            await message.answer(
                text=f"{kun('tashkent')} \n<b>{Viloyat('tashkent')}</b> hududida kutilayotgan ob-havo.\n\n"
                     f"🌡 {harorat('tashkent')}...{min('tashkent')} , {obhavo('tashkent')}\n\n"
                     f"<b>Tong</b> : {tong('tashkent')} \n"
                     f"<b>Kun</b> : {kunh('tashkent')}\n"
                     f"<b>Oqshom</b> : {oqshom('tashkent')}\n"
                     f"_________________________________________\n"
                     f" {Oy('tashkent')}\n"
                     f"_________________________________________\n"
                     f"{Namlik('tashkent')}\n"
                     f"Doimiy ob-havo ma'lumotlari  <a href='https://t.me/WeatherUZB_Robot'>Ob-Havo</a>\n"
                     f"<b>Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing</b>",
                reply_markup=WeatherUZ, disable_web_page_preview=True)

