from pyowm import OWM
import telebot

from pyowm.utils.config import get_default_config
get_default_config()['language'] = 'ru'

owm = OWM('5ce13fe2ed16fa5a4f3683c6684c89f9')
bot = telebot.TeleBot("1023885403:AAH9d2s9aNXQb_G1XsK-K_WDKXKGC_z2C3c")

@bot.message_handler(content_types=['text'])

def send_welcome(message):
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        temp = w.temperature('celsius')['temp']

        answer = "В городе " + message.text + " сейчас температура: " + str(temp) + " по Цельсию, " + w.detailed_status + '\n'

        if (temp >= 0 and temp < 15):
            answer += 'На улице холодновато, оденься потеплее.'
        elif (temp >= 15 and temp < 22):
            answer += 'На улице приемлемо, оденься обычно.'
        elif (temp >= 22 and temp < 27):
            answer += 'На улице очень жарко, одевай шорты.'
    except:
        answer = "Город не найден"

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True, timeout=120)

