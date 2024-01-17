def main():
    
    nums = [10, 5, 2, 8, 7, 1, 15, 5, 3, 4]
    insert_sort(nums)
    print("Insert Sorted Array: ", (nums))

def insert_sort(arr):

    for i in range( 1, len(arr) ):
        j = i 
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
            # To see the state of the array at each step of the iteration, uncomment the print statement below
            # print(arr)


if __name__ == "__main__":
    main()