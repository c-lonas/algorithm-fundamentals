fn main() {
    let mut nums = [10, 5, 2, 8, 7, 1, 15, 5, 3, 4];
    let n = nums.len() - 1;
    quick_sort(&mut nums, 0, n);
    println!("quick sorted nums: {:?}", nums);

}

fn quick_sort<T: Ord>(arr: &mut [T], low: usize, high: usize) {
    if low < high {
        
        let pivot_index = partition_helper(arr, low, high);
        if pivot_index > 0 {
            quick_sort(arr, low, pivot_index - 1);
        }
        quick_sort(arr, pivot_index + 1, high);
    }
}

fn partition_helper<T: Ord>(arr: &mut [T], mut l: usize, mut r: usize) -> usize {
    let pivot_index = (l + r) / 2;
    while l <= r {

        while arr[l] < arr[pivot_index] {
            l += 1;
        }

        while arr[r] > arr[pivot_index] {
            r = r.saturating_sub(1); // To prevent underflow
        }

        if l <= r {
            arr.swap(l, r);
            if l != r {
                l += 1;
                r = r.saturating_sub(1);
            } else {
                l += 1;
            }
        }
    }
    l
}
