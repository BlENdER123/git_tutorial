def my_first_func(param):
    return param

var = my_first_func(123)

print(var)

def print_name(name):
    '''Описание функци'''
    print('1234' + name()) #здесь вызываем переданную функцию со скобками, так как в аргументе передали без скобок
    print(name)

def read_name():
    return '::: ' + input('Введите ваше имя: ') + ' :::'

print_name( read_name ) #передаем в качестве аргумента функции другую функцию