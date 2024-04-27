use proconio::{fastout, input};
use std::cmp::max;

fn main() {
    input! {a: [i32;9],b:[i32;8]}
    let ans = a.iter().sum::<i32>() + 1 - b.iter().sum::<i32>();
    println!("{}", max(0, ans));
}
