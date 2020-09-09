# вход на сайт с помощью парсера
import requests
from bs4 import BeautifulSoup as BS 

s = requests.Session()

# берем csrf токен для авторизации
html = s.get('https://smartprogress.do/')
bs = BS(html.content, 'html.parser')
csrf = bs.select('input[name=YII_CSRF_TOKEN]')[0]['value']

# авторизация
payload = {
    'YII_CSRF_TOKEN': csrf,
    'returnUrl:': '/',
    'UserLoginForm[email]': 'zadoroshniy_anton_2003@mail.ru',
    'UserLoginForm[password]': 'H3GpjabKE93J4JB',
    'UserLoginForm[rememberMe]': 1,
}

answer = s.post('https://smartprogress.do/user/login', data=payload)
answer_bs = BS(answer.content, 'html.parser')

print(answer_bs.select('.user-menu__info-text--lvl')[0].text)