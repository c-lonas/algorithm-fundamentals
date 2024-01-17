def main():
    
    myArray = [0, 2, 4, 5, 6, 7, 9, 10, 15, 22]
    myTarget = 4

    print("Iterative Binary Search")
    print(iterative_binary_search(myArray, myTarget))

    print("Recursive Binary Search")
    print(recursive_binary_search(myArray, myTarget, 0, len(myArray) - 1))

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

# Recursive
def recursive_binary_search(arr, target, low, high):

    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            return recursive_binary_search(arr, target, low, mid - 1)

        elif arr[mid] < target:
            return recursive_binary_search(arr, target, mid + 1, high)
    else:
        return -1


if __name__ == "__main__":
    main()