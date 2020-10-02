test = "Привет"

print(test[1])

array = [1,2,3,4,5,6]

array[1] = 1

array += [7,8,9]
# array.append(['Hello'])

print(array)
print('В массиве находится ' + str(len(array)) + ' элементов')

array.remove(1)
print(max(array))
print(array.count(1))

if 1 in array:
    print( 'the 1 is in array' )

if 10 not in array:
    print( 'the 10 is not in the array' )

print('arrays 2 ---------------')

numbers = list(range(20, 50, 2))

for elem in numbers:
    print( str(elem) + ' elem' )

for test in range(5):
    print('this code print 5 times')
