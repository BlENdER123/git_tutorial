from pyowm import OWM

city = input("Какой город вас интересует?: ")

from pyowm.utils.config import get_default_config
get_default_config()['language'] = 'ru'

owm = OWM('5ce13fe2ed16fa5a4f3683c6684c89f9')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
temp = w.temperature('celsius')['temp']
if (temp >= 0 and temp < 15):
    print('На улице холодновато, оденься потеплее.')
elif (temp >= 15 and temp < 22):
    print('На улице приемлемо, оденься обычно.')
elif (temp >= 22 and temp < 27):
    print('На улице очень жарко, одевай шорты.')

print("В городе " + city + " сейчас температура: " + str(temp) + " по Цельсию, " + w.detailed_status)