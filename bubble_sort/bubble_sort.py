def main():
    
    nums = [10, 5, 2, 8, 7 , 1]
    bubble_sort(nums)
    print("Sorted array: ", nums)

def bubble_sort(arr):

    for i in range(len(arr)):
        # Uncomment the print statements to visualize the state of the array at each iteration of the loops
        # print("Outer loop: ", i)
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # print(arr)


if __name__ == "__main__":
    main()