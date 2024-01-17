- Time complexity: Average and worst O(n²), best case O(n) if it is already sorted
- Space complexity: O(1)
- The quadratic time complexity makes this unsuitable for most not-small arrays where performance is a concern, but like bubble sort, it is notable for being a conceptually simple algorithm that is useful for education.

# Conceptual Overview

Insertion sort iterates through an array, starting at the 2nd element (index 1), and at each iteration checking the element against the element at the index before it. If it's smaller, they swap places, and then continues until reaching the beginning of the array.

This requires a nested loop- an outer loop that progress through each index of the array, and an inner loop that handles the swapping/inserting of the smaller elements continually towards the beginning of the array. It is this nesting that gives the algorthim it's quadratic time complexity.

It is kind of like a reverse Bubble Sort, where instead of 'bubbling' the larger elements to the end of the array, the smaller elements continually get 'inserted' closer to the beginning of the array.

# Logic Walkthrough

The code here is straightforward and essentially the same as the conceptual overview, so just a couple of notes:

1) It's important that you don't do a `for each` loop. You need `i` and `j` to be indices, so that you can compare positions correctly.

2) The first check in the while loop (`j > 0`) is to prevent an index out of bounds error