from tkinter import *
from tkinter import scrolledtext  
from pyowm import OWM

from pyowm.utils.config import get_default_config
get_default_config()['language'] = 'ru'

owm = OWM('5ce13fe2ed16fa5a4f3683c6684c89f9')

window = Tk()
window.title('Прогноз погоды')
window.geometry('600x500')

def get_weather():
    try:
        mgr = owm.weather_manager()
        city = txt.get()
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temp = w.temperature('celsius')['temp']

        answer = ''

        if (temp >= 0 and temp < 15):
            answer += 'На улице холодновато, оденься потеплее. \n'
        elif (temp >= 15 and temp < 22):
            answer += 'На улице приемлемо, оденься обычно. \n'
        elif (temp >= 22 and temp < 27):
            answer += 'На улице очень жарко, одевай шорты. \n'

        answer += "В городе " + city + " сейчас температура: " + str(temp) + " по Цельсию, " + w.detailed_status

        output.configure(text=answer)
    except:
        output.configure(text='Такого города не существует')


title = Label(window, text='Введите название города', font=('Roboto', 30), padx=60, pady=10)
title.grid(column = 0, row = 0)

txt = Entry(window, width = 25)
txt.grid(column = 0, row = 1)

btn = Button(window, text='Узнать погоду', padx = 5, pady = 5, command = get_weather)
btn.grid(column = 0, row = 2)

output = Label(window, text='...', font=('Roboto', 12))
output.grid(column=0, row=3)  

window.mainloop()
