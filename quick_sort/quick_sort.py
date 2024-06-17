def main():

    nums = [3, 10, 5, 2, 8, 7, 1, 15, 6, 11, 4]
    # print(quick_sort_list_comprehension(nums))

    quick_sort(nums, 0, len(nums) - 1)
    print("Quicksorted Array: ", (nums))

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = qs_partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def qs_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
    

# The list comprehension implementation does NOT sort in place. 
# Calling it above I simply print out the results so the original array will remain unsorted for use
# in the next quick sort implementation.
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