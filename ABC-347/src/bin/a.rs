use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,k:usize, aa:[usize;n]}

    let ans = aa
        .iter()
        .filter(|&a| a % k == 0)
        .map(|a| a / k)
        .collect::<Vec<usize>>();
    println!("{}", ans.iter().join(" "));
}
