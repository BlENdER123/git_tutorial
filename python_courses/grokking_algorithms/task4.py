def sum(list): # подсчет суммы всех элементов массива
    if list == []:
        return 0
    return list[0] + sum(list[1:]) 

# print(sum([1,2,3,4,5]))

def elems(list): # подсчет количествва элементов массива
    if list == []:
        return 0
    return 1 + elems(list[1:])

# print(elems([5,4,3,5]))

def max(list): # нахождение максимального элемента массива
    if len(list) == 2:
        if(list[0] > list[1]):
            return list[0]
        else:
            return list[1]

    sub_max = max(list[1:])

    if(list[0] > sub_max):
        return list[0]
    else:
        return sub_max

# print(max([1,2,3,45,6,7]))

array = [50,2,3]

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        p = array[0]
        less = [i for i in array[1:] if i <= p]
        greater = [i for i in array[1:] if i > p]

        return quicksort(less) + [p] + quicksort(greater)

print(quicksort(array))
