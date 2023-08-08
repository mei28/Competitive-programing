use proconio::{fastout, input};
use std::cmp::max;

#[fastout]
fn main() {
    input! {n:usize, a:[i32;n]}
    let mut ans = 0;

    for i in 1..n {
        let diff = a[0] - a[i];
        if diff <= 0 {
            ans = max(ans,   diff.abs() + 1);
        }
    }
    println!("{}", ans);
}

