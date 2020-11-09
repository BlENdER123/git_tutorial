answer = input("Хотите добавить нового голосуещего? (1,0) : ")

voted = {
    "Anton" : True,
    "Tom" : True
    }
def check_voter(name):
    if voted.get(name):
        print("такой голосующий уже есть")
    else:
        voted[name] = True
        print("вы успешно зарегистрированы")

while(answer == "1"):
    name = input("Введите имя : ")
    check_voter(name)
    answer = input("Хотите добавить нового голосуещего? (1,0) : ")