use itertools::Itertools;
use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {n:usize,ss :[String;n]}
    println!("{}", ss.iter().rev().join("\n"));
}
