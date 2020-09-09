# игра висилица

print('Привет\n Это игра под название "Висилица"\n Суть игры угадать слово по буквам, количество попыток ограничено! \n Поехали!')

# задаем слово которое будет отгадывать игрок
secret_word =  'Сутолока' #input('Введите секретное слово : ')

# прописываем состояния висилицы
stages = [
    '    +---+ \n    0   | \n   /|\  | \n   / \  | \n       ---',
    '    +---+ \n    0   | \n   /|\  | \n   /    | \n       ---',
    '    +---+ \n    0   | \n   /|\  | \n        | \n       ---',
    '    +---+ \n    0   | \n   /|   | \n        | \n       ---',
    '    +---+ \n    0   | \n    |   | \n        | \n       ---',
    '    +---+ \n    0   | \n        | \n        | \n       ---',
    '    +---+ \n        | \n        | \n        | \n       ---',
]
# переменаая отслеживающая количество ошибок игрока
mistakes = 0
# массив в котором будут хранится все нерпавильные буквы игрока
wrong_letters = []
# массив в котром будут хранится буквы которые угадал игрок
new_letter = []
# заполнение массива прочерками 
for i in range(len(secret_word)):
    new_letter.insert(0, '_')

# функция отвечающая за вывод различных сообщений
def print_result(text):
    print()
    print('----------')
    print()
    print(text)
    print()
    print('----------')
    print()

# функция для правильным ответом
def right_answer():
    print_result('Верная буква!')
    print_info()

# функция для неправильного ответа
def wrong_answer(letter):
    global mistakes

    # соединяем массив в строку чтобы можно было проверить есть ли в нем повторяющиеся неверные буквы
    wrong_letters_string = ''.join(wrong_letters)
    # проверяем на наличие повторов
    if letter in wrong_letters_string:
        print_result('Такая буква уже есть!')
        print_info()
    else:
        wrong_letters.insert(-1, letter + ' ')

        print_result('Неверная буква!')

        mistakes += 1
        # отслеживание пройгрыша игрока
        if(mistakes+1 < len(stages)):
            print_info()
        else:
            print_result('К сожалению вы проиграли!')
            exit()
    
# основная функция
def print_info():
    # выводим висилицу на экран
    print(stages[mistakes])

    # выводим то что уже угадал игрок
    print('Слово : ')
    print(' '.join(new_letter))

    # выводим неверные буквы игрока
    print('Неверные буквы : ')
    wrong_letters_string = ', '.join(wrong_letters)
    print(wrong_letters_string)
    
    ask_letter = input('Введите букву : ')

    # проверяем чтобы игрок не ввел больше 1 символа
    if len(ask_letter) > 1:
        print_result('Введите только 1 символ!')
        print_info()
    else:
        # переводим загаданное слово в массив чтобы проверить угадал ли игрок букву
        secret_word_array = list(secret_word)
        # переменная костыль, чтобы приводить буквы к одному регистру и в дальнейшем их сравнивать
        right_answer_status = False

        for i in range(len(secret_word_array)):
            if ask_letter.lower() == secret_word_array[int(i)].lower():
                right_answer_status = True
                # заменяем прочерк на угаданную букву
                new_letter[i] = ask_letter
                # отслеживание победы игрока
                if ('_' not in new_letter):
                    print_result('Поздравляю, вы выйграли! Слово - ' + secret_word
                    )
                    exit()
            else: 
                if right_answer_status == True:
                    pass
                else:
                    right_answer_status = False

        # выводим игрока информацию про букву
        if (ask_letter in secret_word) or (right_answer_status):
            right_answer()
        else:
            wrong_answer(ask_letter)

print_info()
