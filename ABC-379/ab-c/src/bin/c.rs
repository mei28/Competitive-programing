use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        m: usize,
        x: [usize; m],
        a: [usize; m]
    }

    let mut stones = HashMap::new();
    for i in 0..m {
        stones.insert(x[i], a[i]);
    }

    let total_stones: usize = stones.values().sum();
    if total_stones < n {
        println!("-1");
        return;
    }

    let mut operations = 0;
    let mut surplus = 0;

    for i in 1..=n {
        let stones_in_cell = *stones.get(&i).unwrap_or(&0) + surplus;

        if stones_in_cell < 1 {
            println!("-1");
            return;
        }

        surplus = stones_in_cell - 1;
        operations += surplus;
    }

    println!("{}", operations);
}

