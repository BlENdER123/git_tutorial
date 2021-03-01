def smallest_numb(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if(smallest > arr[i]):
            smallest = arr[i]
            smallest_index = i
    return smallest_index        
        
def sort(arr):
    sort_arr = []
    for j in range(len(arr)):
        smallest = smallest_numb(arr)
        sort_arr.append(arr.pop(smallest))
    return sort_arr

numbers = [0,2,1,5,7,8,9]

print(sort(numbers))