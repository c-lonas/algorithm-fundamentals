
# Iterative

def iterative_binary_search(arr, target):
    low =  0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        
        mid = (low + high) // 2
        if target > arr[mid]:
            low = mid + 1

        elif target < arr[mid]:
            high = mid - 1

        else:
            return mid
        
    return -1


myArray = [0, 2, 4, 5, 6, 7, 9, 10, 15, 22]
myTarget = 4


print(iterative_binary_search(myArray, myTarget))