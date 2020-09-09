# weather - api
from pyowm import OWM

from pyowm.utils.config import get_default_config
get_default_config()['language'] = 'ru'

# telegram bot - api
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# token`s for bot
import config

owm = OWM(config.OWM)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# start - command
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет, я умею показывать погоду в любых городах!')

# help - command
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('Напиши мне любой город и я скажу погоду в нем')

# test - command
@dp.message_handler(commands=['test1'])
async def test1_command(message: types.Message):
    msg1 = message.text.split('/test1')
    await message.reply('Тестовая команда')
    await bot.send_message(message.from_user.id, msg1[1])

# basic message
@dp.message_handler()
async def weather_message(msg: types.Message):
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(msg.text)
        w = observation.weather
        temp = w.temperature('celsius')['temp']

        answer = "В городе " + msg.text + " сейчас температура: " + str(temp) + " по Цельсию, " + w.detailed_status + '\n'

        await bot.send_message(msg.from_user.id, answer)
    except:
        await bot.send_message(msg.from_user.id, 'Название города введено неверно')

if __name__ == '__main__':
    executor.start_polling(dp)