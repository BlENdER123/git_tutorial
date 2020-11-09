def f(x):
    if(x == 0):
        return 0
    if(x == 1):
        return 1
    return f(x-1) + f(x-2)

# for i in range(100):
#     print(f(i))

def fact(x):
    if(x==1):
        return 1
    return x*fact(x-1)

print(fact(10))