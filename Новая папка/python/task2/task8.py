#Посчитайте, сколько раз символ встречается в строке.
string = 'Adasksdskdd kjf'

def func1(str1, word):
    for el in range(len(str1)):
        if word == str1[el]:
            print(word)

func1(string, 'd')