#3 задача квадрат

side = float(input('Введите сторону квадрата'))

def square(side):
    perim = side * 4
    area = side**2
    diag = side*(2**0.5)
    return perim,area,diag

test = square(side)

print(test)