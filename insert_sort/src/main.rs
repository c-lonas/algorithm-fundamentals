fn main() {
    println!("Hello, world!");

    let nums = [10, 5, 2, 8, 7, 1, 15, 5, 3, 4];

    println!("Insert Sorted Array: ", nums)
}

fn insert_sort<T: Ord>(arr: &mut [T]) {

    for i in 1..arr.len() {

        let mut j = i;
        while j > 0 && arr[j] < arr[j - 1]{
                arr.swap(j, j - 1);
                j -= 1;
        }
    }
}