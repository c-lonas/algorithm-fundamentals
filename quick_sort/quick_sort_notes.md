- Time complexity
    - Average: O (n log n)
    - Worst case: O(n²) - when smallest/largest element always picked as pivot
- Space complexity: O(log n) - due to recursive stack space
- Stable: false - equal elements are not guaranteed to remain in their initial relative order
- Type: Divide-and-conquer
- In place: true
- Good for large arrays
- Good when average performance matters more than worst case

# Conceptual Overview

Like indicated above, this is a 'divider-and-conquer' type algorithm. 

It selects a 'pivot' element from the array, and then partitions the rest of the elements into two sub-arrays based on whether the elements are greater or less than the pivot. Each of these sub-arrays are then sorted recursively.


