#Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def func1(a,b):
    a_b = []
    for elemA in a:
        for elemB in b:
            if(elemA == elemB):
                a_b.append(elemA)
    return a_b

test = func1(a,b)
print(test)