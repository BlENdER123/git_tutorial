#Найдите три ключа с самыми высокими значениями в словаре
my_dict = {'a': 500, 'b': 5874, 'c': 560,'d': 400, 'e': 5874, 'f': 20}

# def func1(a):
#     a1 = None
#     a2 = None
#     for elem1 in a:
#         for elem2 in a:
#             if(a[elem1] > a[elem2]):
#                 a1 = a[elem1]
    
#     return a1,a2

# test = func1(my_dict)

print(sorted(my_dict, key=my_dict.get, reverse=True)[:3])