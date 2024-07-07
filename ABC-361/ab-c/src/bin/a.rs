use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n:usize,
        k:usize,
        x:usize,
        mut aa: [usize;n]
    }

    aa.insert(k, x);
    println!("{}", aa.iter().join(" "));
}
