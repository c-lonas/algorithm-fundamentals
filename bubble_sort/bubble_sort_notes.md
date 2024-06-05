# Bubble Sort

- Time complexity: O(n²) (both average and worst case)
    - There are variations on the basic Bubble Sort that have an early termination case in the event an iteration completes without needing to swap anything, meaning it is already sorted. With this variation, the best case time complexity becomes O(n)
- Space complexity: O(1)
- Stable sorting algorithm (equal elements retain their original ordering)
- Good for learning due to both conceptual and technical simplicity. For actual performance, never use this, use something like quicksort or mergesort, etc.

# Conceptual Overview

Bubble sort hinges around the nested `for loop`- which incidentally, is also why this has poor performance (`O(n²)`)

The idea of bubble sort is simple and easy to think through, which is why it is more commonly used in educational settings than it is actually applied as to sort in the real world. 

You iterate through your array, and check whether or not the first element is greater than the one to its right. If it is, they switch places. You continue until you reach the end of the array, and then repeat the process with each remaining element in the array.

The biggest elements getting sorted first as they 'bubble up' towards the end of the array in each iteration, and the smallest elements falling into place last.

That's it.


# Logic Walkthrough

Walking through the code here seems a little superfluous as it is basically the same as the conceptual overview. Just a few notes:

1) It's important that you don't do `for each` loops. You need `i` and `j` to be indices, so that you can compare positions correctly.

2) The inner loop is set to the length of array, minus `i` minus `1`. The minus `1` ensures that you don't get an index out of bounds. The minus `i` ensures that on each iteration of the outer loop, the inner loop gets smaller. This is because the end of the array gets sorted first, so you don't need to keep iterating through it after it is sorted.
