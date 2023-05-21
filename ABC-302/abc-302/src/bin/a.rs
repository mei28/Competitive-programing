use cmp::{max, min, Reverse};
use proconio::{fastout, input, marker::*};
use std::collections::*;
use std::*;

#[fastout]
fn main() {
    input! {
        a: usize,
        b: usize,
    }

    let ans = (a + b - 1) / b;
    println!("{}", ans);
}
