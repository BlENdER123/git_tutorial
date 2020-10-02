import requests

response = requests.get('https://api.github.com')

if(response.status_code == 200):
    print("Запрос выполнен успешно!")
    print(response.headers)
else:
    print("Ошибка при выполнении запроса")