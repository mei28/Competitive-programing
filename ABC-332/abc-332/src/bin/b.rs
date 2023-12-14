use proconio::{fastout, input};
use std::cmp::min;

#[fastout]
fn main() {
    input! {k:usize,g:usize,m:usize}

    let mut glass = 0;
    let mut mag = 0;

    for i in 0..k {
        if glass >= g {
            glass = 0;
        } else if mag == 0 {
            mag = m
        } else {
            let diff = (g - glass).min(mag);
            glass += diff;
            mag -= diff;
        }
    }

    println!("{} {}", glass, mag);
}
