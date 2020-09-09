list1 = [1,2,3,4,5,6,7,8,9,0,5,6,7,8]
list2 = list1[::-1] #простой способ получить перевернутый массив


what = int(input('Какой топ цифр? : '))

if what > 0:
    print(list1[:what])
elif what < 0:
    print(list1[what:][::-1])