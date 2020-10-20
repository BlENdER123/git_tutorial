import requests
from bs4 import BeautifulSoup as BS
import time
import telebot

print('Привет, это Telegram парсер, \nВведи нужные данные и запускай меня')
sleep_time = int(input('Введите интервал для проверки постов ( min. 1 минута, max. 60 мин ) : '))

while (sleep_time < 1) or (sleep_time > 60):
    print('Введите правильное время')
    sleep_time = int(input('Введите интервал для проверки постов ( min. 1 минута, max. 60 мин ) : '))

chn = input('Введите id вашего канала (в формате @channel_name) : ')

while (chn[0] != '@'):
    print('Введите правильное имя канала')
    chn = input('Введите id вашего канала (в формате @channel_name) : ')
    if (chn[0] == '@'):
        break

print('Go!')

# токен для бота и id телеграмм канала
BOT_TOKEN = '1321213395:AAGKL_ymQGE1FZ0Te4h-y97quQO9NWtxqfc'
CHANNEL_NAME = '@world_news_chn'

# функция по получению новых постов
def get_new_post():
    # парсим нужный сайт

    r = requests.get('https://www.livejournal.com/rsearch?tags=%D0%BC%D0%B0%D1%81%D0%BE%D0%BD%D1%8B&searchArea=post')
    html = BS(r.content, 'html.parser')

    print(html)

    # вытаскиваем все ссылки
    title = html.select('.rsearch-note__caption')
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
    title = html.select('.b-singlepost-title')
    title = title[0].text

    text = html.select('.b-singlepost-body')
    # text_arr = html.select('.b-singlepost-body')
    # text = ''

    # соединяем текст в одну строчку
    # for el in range(len(text_arr)):
    #     text += str(text_arr[el].text)+'\n'

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
        print(lastpost)
        time.sleep(1)
    else:
        file.write('|||'+str(lastpost))
        # отправляем пост на канал
        bot = telebot.TeleBot(BOT_TOKEN)
        bot.send_message(CHANNEL_NAME, f'{title}\n\n{text}<a href="{pic}">&#160;</a>', parse_mode='HTML')
        time.sleep(1)
    file.close

# бесконечная проверка с произвольным перерывом
# if __name__ == '__main__':
#     while True:
#         get_new_post()
#         print(f'Следущая проверка будет через {sleep_time} минут')
#         time.sleep(sleep_time*60)

while True:
    get_new_post()
    print(f'Следущая проверка будет через {sleep_time} минут')
    time.sleep(sleep_time*60)