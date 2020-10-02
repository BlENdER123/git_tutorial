#1 задача простейший калькулятор
a = float(input('Введите первое число :'))
b = float(input('Введите второе число :'))
what = input('Введите операцию(+ , - , * , /) :')

def arithmetic(a,b,what):
    result = 0
    if what == '+':
        result = a + b
    elif what == '-':
        result = a - b
    elif what == '*':
        result = a * b
    elif what == "/":
        result = a / b
    else:
        result = 'Неизвестная команада, повторите попытку еще раз'
    print(result)

arithmetic(a,b,what)

