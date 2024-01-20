def main():

    nums = [10, 5, 2, 8, 7, 1, 15, 5, 3, 4]
    # print(quick_sort_list_comprehension(nums))

    quick_sort(nums, 0, len(nums) - 1)
    print("Quicksorted Array: ", (nums))

def quick_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        pivot = arr[mid]
        pivot_index = partition_helper(arr, low, high, pivot)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition_helper(arr, l, r, pivot):
    
    while l <= r:

        while arr[l] < pivot:
            l += 1
        
        while arr[r] > pivot: 
            r -= 1

        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    return l
    

# The list comprehension implementation does NOT sort in place. 
# Calling it above I simply print out the results so the original array will remain unsorted for use
# in the next quick sort implementation. If you wanted to retain the sorted array, you would just
# store the output in a new variable
def quick_sort_list_comprehension(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort_list_comprehension(less) + [pivot] + quick_sort_list_comprehension(greater)

if __name__ == "__main__":
    main()