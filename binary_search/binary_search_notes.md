# Binary Search

- Binary search requires a sorted array
- Time complexity: O(log n)
- Iterative and recursive variations

## Conceptual Overview

The logic of binary search is straight forward. You split a sorted array into a left half and a right half, and check the element at the middle index of the total array. Check if that value matches the value you are searching for.

If it does, congrats, you're done. 

If the number at the middle index doesn't match and is *higher* than the number you're looking for, then you know there is no point in checking the rest of the numbers in the *right* half of the array- remember, this is a sorted array (or it won't work). You can then discard the right half of the array, and repeat the process looking only at the left half of the array.

If the number at the middle index doesn't match and is *lower* than the number you're looking for, then you know there is no point in checking the rest of the numbers in the *left* half of the array. You can discard the left half of the array, and repeat the process looking only at the right half of the array.

You repeat the process, dividing the array in half at each iteration until you have either found the target, or determined that the array does not contain it.

## Logic Walkthrough
You initialize variables represent pointers to the `low` and `high` indices, and a variable to represent the `mid` point between them. `low` and `mid` are both initialized at `0`, and `high` is initialized at the length of the array, minus `1`.

With an iterative approach, create a `while` loop that continues as long as `low <= high`. That represents that you haven't checked the entire array yet.

Within each loop, you find the `mid` point of the array. If the `target` is greater than the value you found at the `mid` point, then you can rule out the left half of the array. You set `low` to be equal to `mid + 1` for the next iteration. `elif` the target is less than the value at the `mid` point of the array, you rule out the right half of the array, so you set `high` to be equal to `mid - 1`. If the target is neither less than nor greater than the value you have found, than it is equal to it- so you can simply `return mid`


With a recursive approach, you remove the `while` loop- this is being replaced by the recursive function calls.

You first check to make sure that you haven't already checked the entire array, by making sure that your `high` pointer is still greater than or equal to your `low` pointer. If it is, you set your new mid point same as before, and then check the base case- `if arr[mid] == target`.

If not, you need to determine if you are ruling out the left or right half of the array again. However, with the recursive approach, you accomplish this by calling the same function again, passing in `mid - 1` as your argument to the the `high` parameter to rule out the right half of the array, or passing in `mid + 1` as your argument to the `low` parameter to rule out the left half of the array.