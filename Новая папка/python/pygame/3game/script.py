# Игра 'Крестики - Нолики'
import random

print(' Привет\n Это игра под названием "Крестики - Нолики"\n Суть игры заполнить подряд 3 клетки на поле ( Это можно сделать вертикально, горизантально, на искосок )\n Против вас будет играть ИИ ( Искуственный Интелект )\n Поехали!')

# переменные отвечающие за знак игрока и компьютера
player_letter = ' '
comp_letter = ' '

# массив отвечающий за хранение данных о клетках игрового поля
field = [
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
    ' ',
]

# функция которая спрашивает за что будет играть игрок
def get_player_letter():
    global player_letter, comp_letter
    while not(player_letter.upper() == 'X' or player_letter.upper() == 'O'):
        player_letter = input('За что вы будете играть ( O , X ) : ')

    if player_letter.upper() == 'X':
        comp_letter = 'O'
    else:
        comp_letter = 'X'

# функция которая решает кто будет ходить первым рандомно
def who_goes_first():
    print('Сейчас рандом решит кто будет ходить первым !')
    if random.randint(0,1) == 0:
        return 'Человек'
    else:
        return 'Компьютер'

# функция которая выводит игровое поле
def show_field():
    print(
        """
        Разметка игровго поля : 

         7 | 8 | 9
        ---|---|---
         4 | 5 | 6
        ---|---|---
         1 | 2 | 3
        """
    )
    print(
        f"""
        Игровое поле : 

         {field[6]} | {field[7]} | {field[8]}
        ---|---|---
         {field[3]} | {field[4]} | {field[5]}
        ---|---|---
         {field[0]} | {field[1]} | {field[2]}
        """
    )

# функция которая проверяет свободно ли переданная клетка
def is_field_free(letter, field):
    if isinstance(letter, list): # функция isinstance() которая сравнивает переданыые данные с типом которые вы хотите
        for i in letter:
            if field[i-1] == ' ':
                return i-1
    else:
        if field[letter-1] == ' ':
            return True
        else:
            return False

# функция которая делает копия игрового поля ( это нужно для того чтобы ИИ мог определять свои будущие ходы )
def make_field_copy():
    global field
    field_copy = []

    for i in field:
        field_copy.append(i)

    return field_copy

# функция которая проверяет выграл ли опредеенный знак или уже ничья
def is_winner(letter, field):
    global winner, game_end

    if is_field_free([1,2,3,4,5,6,7,8,9], field) == None:
        print('Ничья, клетки закончились')
        exit()
    
    if ( field[0] == letter and field[1] == letter and field[2] == letter ) or ( 
         field[3] == letter and field[4] == letter and field[5] == letter ) or ( 
         field[6] == letter and field[7] == letter and field[8] == letter ) or (
         field[0] == letter and field[3] == letter and field[6] == letter ) or (
         field[1] == letter and field[4] == letter and field[7] == letter ) or (
         field[2] == letter and field[5] == letter and field[8] == letter ) or (
         field[0] == letter and field[4] == letter and field[8] == letter ) or (
         field[2] == letter and field[4] == letter and field[6] == letter ):
            
            return True
    else:
        return False

# функция отвечающая за ход игрока
def player_turn():
    global field, player_letter
    print('Сейчас ваша очередь ходить')
    pl_let = int(input('Введите цифру ( от 1 до 9 ) в соответствии с клеткой которую хотите выбрать : '))

    while not(is_field_free(pl_let, field)):
        print('Эта клетка уже занята, попробуйте другую !')
        pl_let = int(input('Введите цифру ( от 1 до 9 ) в соответствии с клеткой которую хотите выбрать : '))

    field[pl_let-1] = player_letter
    return

# функция отвечающие за ход компьютера
def comp_turn():
    global field, comp_letter
    print('Сейчас ходит ИИ')

    # 1 проверка - ИИ проверяет на копии игрового поля есть ли вариант где он может победить, если нет он переходит к следующей проверке
    for i in range(1,10):
        copy = make_field_copy()
        if is_field_free(i, copy):
            copy[i-1] = comp_letter
            if is_winner(comp_letter, copy):
                print(f'{i} в данном поле мы можем победить')
                field[i-1] = comp_letter
                return 
        
    print('ИИ пока не может сделать победный ход, но я помещаю человеку выйграть')
    
    # 2 проверка - ИИ проверяет на копии игрового поля есть ли вариант где может победить игрок, если есть то ИИ поставит туда свой знак, тем самым помешав игроку выйграть
    for i in range(1,10):
        copy = make_field_copy()
        if is_field_free(i, copy):
            copy[i-1] = player_letter
            if is_winner(player_letter, copy):
                print(f'{i} в данном поле человек может победить, помешаем ему !')
                field[i-1] = comp_letter
                return

    print('Не удалось помешать человеку выйграть')

    # 3 проверка - ИИ проверяет свободны ли углы на игровом поле, чтобы занять их
    if is_field_free([1,3,7,9], field) != None:
        print('Хожу по угловым клеткам !')
        free_field = is_field_free([1,3,7,9], field)
        field[free_field] = comp_letter
        return

    print('Угловые клетки заняты, попробую что-нибудь другое')
    
    # 4 проверка - ИИ проверяет свободен ли центр игрового поля, чтобы занять его
    if is_field_free(5, field):
        print('Ходим в центр !')
        field[5-1] = comp_letter
        return

    print('Центральная клетка занята, попробую что-нибудь другое')

    # 5 проверка - последняя проверка где ИИ пытается поставить свой знак по бокам игрового поля
    if is_field_free([2,4,6,8], field) != None:
        print('Ходим по боковым клеткам')
        free_field = is_field_free([2,4,6,8], field)
        field[free_field] = comp_letter
        return

    print('Все клетки заняты')

# переменная отвечающая за игровой цикл
game_end = False

# переменная чтобы ходы повторялись пока кто то не победит ( или ничья )
winner = False

# игровой цикл
while not game_end:
    # спрашиваем игрока за кого он будет играть
    get_player_letter()

    # показываем игровое поле
    show_field()    

    # определяем кто ходит первый
    first = who_goes_first()
    if(first == 'Человек'):
        player_turn()
        show_field()    
    else:
        comp_turn()
        show_field()
    # цикл чтобы повторялись ходы пока не закончится игра 
    while not winner:
        if(first == 'Человек'):
            comp_turn()
            show_field()
            if(is_winner(comp_letter, field)):
                winner = True
                game_end = True
                print('Компьютеры победили')
                exit()
            player_turn()
            show_field() 
            if(is_winner(player_letter, field)):
                winner = True
                game_end = True
                print('Человек ты превзошел компьютер')
                exit()
        else:
            player_turn()
            show_field()
            if(is_winner(player_letter, field)):
                winner = True
                game_end = True
                print('Человек ты превзошел компьютер') 
                exit()
            comp_turn()
            show_field()
            if(is_winner(comp_letter, field)):
                winner = True
                game_end = True
                print('Компьютеры победили')
                exit()

print('Игра окончена !')
