use std::cmp::Ordering;

fn main() {
    println!("Iterative Binary Search");

    let my_vector = vec![0, 2, 4, 5, 6, 7, 9, 10, 15, 22];
    let my_target = 4;
    let result = binary_search(&my_vector, &my_target);

    match result {
        Some(index) => println!("Found {} at index {}", &my_target, index),
        None => println!("{} not found", &my_target)
    }
}

fn binary_search<T: Ord>(arr: &[T], target: &T) -> Option<usize> {

    let mut low = 0;
    let mut high = arr.len() - 1;

    while low <= high {
        let mid = (low + high) / 2;

        match arr[mid].cmp(target) {
            Ordering::Less => low = mid + 1,
            Ordering::Greater => high = mid - 1,
            Ordering::Equal => return Some(mid)
        }
    }
    None
}