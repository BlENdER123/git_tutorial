arr1 = [1,1,2,2,4,0,34,5,56,237,1]

def arr(arr):
    for el in range(len(arr)):
        if(arr[el] == 237):
            print('err')
        elif(arr[el]%2 == 0):
            print(arr[el])

arr(arr1)