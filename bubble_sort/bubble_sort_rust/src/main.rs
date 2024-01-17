use std::fmt::Debug;

fn main() {

    let mut nums = [10, 5, 2, 8, 7 , 1];
    bubble_sort(&mut nums);
    println!("{:?}", nums);

    // &str also implements the Ord trait, so this works too
    let mut words = ["pear", "apple", "orange", "banana", "kiwi"];
    bubble_sort(&mut words);
    println!("{:?}", words);
}

fn bubble_sort<T: Ord + Debug>(arr: &mut [T]) {

    for i in 0..arr.len() {
        for j in 0..arr.len() - i - 1 {
            // Uncomment the print macro below to see each step of the bubble sort in action
            // println!("{:?}", arr); 
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1)
            }
        }
    }
}