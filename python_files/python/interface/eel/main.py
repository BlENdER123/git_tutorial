import eel
import pyowm
import datetime

from pyowm.utils.config import get_default_config
get_default_config()['language'] = 'ru'

owm = pyowm.OWM('5ce13fe2ed16fa5a4f3683c6684c89f9')

@eel.expose
def get_weather(place):
    try:
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place(place)
        w = observation.weather
        wind_dict_in_meters_per_sec = observation.weather.wind()

        temp = w.temperature('celsius')['temp']

        now = datetime.datetime.now()
        time = {
            'year' : now.year,
            'month' : now.month,
            'day' : now.day,
            'hour' : now.hour,
            'minute' : now.minute}

        return {
            'place' : place,
            'temp' : temp,
            'status' : w.status,
            'time' : time
        }
    except:
        return 'Введите правильное название города'
    

eel.init('web')

eel.start('main.html', size=(700,700))