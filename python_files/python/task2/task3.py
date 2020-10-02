#Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
word = 'АлЛа'

def polin(word):
    word = word.lower()
    lenw = len(word)
    res = True
    for el in range(lenw):
        id = -el-1
        if(word[el] == word[id]):
            res = True
        else:
            return False
    return res

test = polin(word)

print(test)

# Более простые методы

# def is_palindrome(string):
#     return string == ''.join(reversed(string))

# print(is_palindrome('abba'))

# Того же эффекта можно добиться с помощью срезов:

# def is_palindrome(string):
#     return string == string[::-1]

# print(is_palindrome('abba'))