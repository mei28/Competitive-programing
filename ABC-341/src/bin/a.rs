use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize}

    println!("{}", (0..=1).rev().cycle().take(2 * n + 1).join(""));
}
