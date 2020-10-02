import requests
from bs4 import BeautifulSoup as BS
import time
import telebot

from tkinter import *
from tkinter import messagebox, BOTH, END, HORIZONTAL, Tk, scrolledtext, ttk

# токен для бота и id телеграмм канала
BOT_TOKEN = '1321213395:AAGKL_ymQGE1FZ0Te4h-y97quQO9NWtxqfc'
CHANNEL_NAME = '@world_news_chn'

# функция по получению новых постов
def get_new_post():
    # парсим нужный сайт
    r = requests.get('https://rozetked.me/news')
    html = BS(r.content, 'html.parser')

    # вытаскиваем все ссылки
    title = html.select('.post_new-title > a')
    article = title[0].attrs['href']

    # передаем последнюю ссылку на проверку
    print('Первая функция')
    copy_new_post(article)

# функция по записыванию новых постов в специальный файл
def copy_new_post(article):
    # file = open('database.txt', 'r+')

    # file_text = str(file.read())
    # file_text = file_text.split('|||')
    
    # теперь парсим ссылку на последнюю статью
    r = requests.get(article)
    html = BS(r.content, 'html.parser')

    # достаем от туда заголовок и текст
    title = html.select('.n_title')
    title = title[0].text
    text_arr = html.select('#news-data>p')
    text = ''

    # соединяем текст в одну строчку
    for el in range(len(text_arr)):
        text += str(text_arr[el].text)+'\n'

    # пробуем достать картинку ( ее может и не быть )
    try:
        src = html.select('.post-main-img>img')[0].attrs['src']
        url = 'https://rozetked.me' + src
    except:
        print('Не удалось найти изображение в статье')
        url = ''
    
    # передаем все данные на отправку
    print('Вторая функция')
    send_post(text, url, article, title)

# функция по отправке постов
def send_post(text, pic, lastpost, title):
    # открываем нашу "базу данных"
    file = open('database.txt', 'r+')
    file_text = str(file.read())
    file_text = file_text.split('|||')
    
    # проверяем был ли этот пост уже опубликован
    if(str(lastpost) == str(file_text[-1])):
        print('Пока новых новостей нет')
        time.sleep(1)
    else:
        file.write('|||'+str(lastpost))
        # отправляем пост на канал
        bot = telebot.TeleBot(BOT_TOKEN)
        bot.send_message(CHANNEL_NAME, f'{title}\n\n{text}<a href="{pic}">&#160;</a>', parse_mode='HTML')
        time.sleep(1)
    print('Третья функция')
    file.close
    for i in range(10):
        print(f'прошло {i} секунд')
        time.sleep(2)
    get_new_post()

# создание окна
window = Tk()

# заголовок для окна
window.title('Парсер для Telegram')

def start():
    console.configure(state=NORMAL)
    console.insert(END,'Сон на 10 минут\n')
    console.configure(state=DISABLED)
    print('11111')
    time_sleep = int(win_time.get())
    if(time_sleep < 1) or (time_sleep > 60):
        messagebox.showinfo('Ошибка', 'Введите время в промежутке от 1 минуты до 60 минут')
        return

    channel = win_key.get()
    if(channel[0] != '@'):
        messagebox.showinfo('Ошибка', 'Введите id канала привильно в формате @channel_name')
        return

    # бесконечная проверка с произвольным перерывом
    if __name__ == '__main__':
        get_new_post()
        # while True:
        #     get_new_post()
        #     print('цикл закончен')
        #     console.configure(state=NORMAL)
        #     console.insert(END,'Сон на 10 минут')
        #     console.configure(state=DISABLED)
        #     print('цикл закончен')
        #     time.sleep(10*60)
    print(f'{win_time.get()} {win_key.get()}')

# центральный текст
win_title = Label(window, text='Привет, это Telegram парсер, \nвведи нужные данные и запускай меня', font=('Roboto', 18))
win_title.pack(padx=15, pady=15)

# поле для ввода времени
win_time_text = Label(window, text = 'Введите интервал для проверки постов \n( min. 1 минута, max. 60 мин )', font=('Roboto', 10))
win_time_text.pack()
win_time = Entry(window, width = 20)
win_time.pack()

# поле для ввода канала
win_key_text = Label(window, text = 'Введите id вашего канала \n(в формате @channel_name)', font=('Roboto', 10))
win_key_text.pack()
win_key = Entry(window, width = 20)
win_key.pack()

# кнопка старта
start_btn = Button(window, text = 'Запуск', bg='#2159FF', fg='#fff', command=start)
start_btn.pack()

console = scrolledtext.ScrolledText(window,height=13, state=DISABLED)
console.pack()


# размеры окна
window.geometry('470x600')

# цикл для программы
window.mainloop()




