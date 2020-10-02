# парсер которые берет все популярные статьи с сайта
import requests
from bs4 import BeautifulSoup as BS 

pages = 4
page = []

#цикл for для того чтобы добавить в массив все страницы с которых нужно спарсить контент, range(1, pages+1): такая конструкция нужна потому что страницы начинаются с 1
for x in range(1, pages+1):
    page.append('https://stopgame.ru/review/new/stopchoice/p' + str(x))

for v in range(len(page)):
    r = requests.get(page[v])
    html = BS(r.content, 'html.parser')

    for el in html.select('.item.article-summary'):
        title = el.select('.caption > a')
        print(title[0].text)