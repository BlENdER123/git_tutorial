import requests
from bs4 import BeautifulSoup as BS
import time
import telebot

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
        bot.send_message(CHANNEL_NAME, "123")
        # bot.send_message(CHANNEL_NAME, f'{title}\n\n{text}<a href="{pic}">&#160;</a>', parse_mode='HTML')
        time.sleep(1)
    file.close

# бесконечная проверка с произвольным перерывом
if __name__ == '__main__':
    while True:
        get_new_post()
        time.sleep(10)