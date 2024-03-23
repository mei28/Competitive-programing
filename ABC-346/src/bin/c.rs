use proconio::{fastout, input};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {n:usize,k:usize,aa:[usize;n]}
    let ans = (1 + k) * k / 2;
    let sum = aa
        .into_iter()
        .collect::<HashSet<usize>>()
        .iter()
        .filter(|&x| *x <= k)
        .sum::<usize>();
    println!("{}", ans - sum);
}
