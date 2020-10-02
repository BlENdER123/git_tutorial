#Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить невозможно, выбросите исключение.
name = 'te.st.txt'

def name_file(name):
    try:
        arr = name.split('.')
        return arr[-1]
    except:
        return 'Ошибка'


test = name_file(name)

print(test)