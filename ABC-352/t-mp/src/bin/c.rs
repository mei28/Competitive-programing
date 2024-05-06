use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n:usize,
        AB: [(usize, usize); n]
    }

    let a_sum = AB.iter().map(|(a, _)| a).sum::<usize>();
    let diff = *AB
        .iter()
        .map(|(a, b)| b - a)
        .collect::<Vec<usize>>()
        .iter()
        .max()
        .unwrap();

    println!("{}", a_sum + diff);
}
