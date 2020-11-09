# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as BS
import time
import telebot

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


print('Привет, это Telegram парсер, \nВведи нужные данные и запускай меня')
sleep_time = int(input('Введите интервал для проверки постов ( min. 1 минута, max. 60 мин ) : '))

while (sleep_time < 1) or (sleep_time > 60):
    print('Введите правильное время')
    sleep_time = int(input('Введите интервал для проверки постов ( min. 1 минута, max. 60 мин ) : '))


print('Go!')

# токен для бота и id телеграмм канала
BOT_TOKEN = '1230947315:AAGNOhoXoCDErUKdcXlL9QTGw4_cihOtGyU' #   
CHANNEL_NAME = '474103257' #   

# функция по получению новых постов
def get_new_post():
    # парсим нужный сайт

    r = requests.get('https://победа-63.рф/catalog/search/?cg=&c=&k=%D0%BC%D0%BE%D0%B4%D0%B5%D0%BC')
    html = BS(r.content, 'html.parser')

    # вытаскиваем все ссылки

    article = html.find("div", {"am-card":["normal"]}).find(("div", {"am-card-info":[""]})).find("a").attrs["href"]

    # передаем последнюю ссылку на проверку
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
    title = html.find("div", {"am-container":["product"]}).find("h1", {"am-text":["block_title"]}).text

    # пробуем достать картинку ( ее может и не быть )
    
    # try:
    #     src = html.find("div", {"am-image":["photo_1"]}).find("img").attrs["src"]
    #     url = 'https://самара.победа-63.рф' + src
    # except:
    #     print('Не удалось найти изображение в статье')
    #     url = ''
    url = ''

    # передаем все данные на отправку
    send_post(url, article, title)

# функция по отправке постов
def send_post(pic, lastpost, title):
    # открываем нашу "базу данных"
    file = open('database.txt', 'r+')
    file_text = str(file.read())
    file_text = file_text.split('|||')
    
    # проверяем был ли этот пост уже опубликован
    post_public = True
    for i in file_text:
        if(str(i) == str(lastpost)):
            print('Пока новых новостей нет')
            print(lastpost)
            time.sleep(1)
            post_public = False

    if(post_public == True):
        file.write('|||'+str(lastpost))
        # отправляем пост на канал
        bot = telebot.TeleBot(BOT_TOKEN)
        bot.send_message(CHANNEL_NAME, 'Появился новый товар\n' + title + '\n ' + lastpost) # 'Появился новый товар\n' + title + '\n ' + lastpost
        # bot.send_message(CHANNEL_NAME, f'Появился новый товар\n{title}\n<a href="{pic}">&#160;</a>\n {lastpost}', parse_mode='html')
        time.sleep(1)
    file.close
    # if(str(lastpost) == str(file_text[-1])):
    #     print('Пока новых новостей нет')
    #     print(lastpost)
    #     time.sleep(1)
    # else:
    #     file.write('|||'+str(lastpost))
    #     # отправляем пост на канал
    #     bot = telebot.TeleBot(BOT_TOKEN)
    #     bot.send_message(CHANNEL_NAME, 'Появился новый товар\n' + title + '\n ' + lastpost) # 'Появился новый товар\n' + title + '\n ' + lastpost
    #     # bot.send_message(CHANNEL_NAME, f'Появился новый товар\n{title}\n<a href="{pic}">&#160;</a>\n {lastpost}', parse_mode='html')
    #     time.sleep(1)
    # file.close

while True:
    get_new_post()
    print('Следущая проверка будет через ' + str(sleep_time) + ' минут')
    time.sleep(sleep_time*60)