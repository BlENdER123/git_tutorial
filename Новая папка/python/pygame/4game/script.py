# -*- coding: utf8 -*- 
# игра 'Угадай число'
import random

print(' Привет \n Это игра под название "Угадай число" \n Суть игры угадать 3 - значное число за 10 попыток \n В течении игры тебе будут даваться различные подсказки \n Холодно - ни одна цифра не угадана \n Тепло - отгадана одна цифра, но не угадана ее позиция \n Горячо - угадана цифра и ее позиция')

attempts = 0

def get_secret_number():
    secret = ''
    numbers = list(range(10))
    random.shuffle(numbers)
    for i in range(3):
        secret += str(numbers[i])
    return secret

def player_turn():
    global attempts, game_end
    attempts += 1
    if attempts >= 11:
        print('У вас закончились попытки')
        game_end = True
        return

    print(f'Попытка № {attempts}')

    pl_num = input('Введите трехзначное число : ')

    while len(pl_num) != 3:
        pl_num = input('Введите трехзначное число : ')

    if pl_num == secret_numb:
        print('Вы угадали !')
        game_end = True
        return
    
    status = []

    for c in range(3):
        if pl_num[c] == secret_numb[c]:
            status.append('Горячо')
        elif pl_num[c] in secret_numb:
            status.append('Тепло')

    # for i in range(3):
    #     for v in range(3):
    #         if (pl_num[i] == secret_numb[v]) and (i != v):
    #             status.append('Тепло')

    if status == []:
        status.append('Холодно')
    
    for b in range(len(status)):
        print(status[b])

game_end = False

secret_numb = get_secret_number()

while not game_end:
    player_turn()
    
print('Игра окончена')