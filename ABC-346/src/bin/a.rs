use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, aa: [usize;n]}
    println!("{}", (0..n - 1).map(|i| aa[i] * aa[i + 1]).join(" "));
}
