use proconio::{fastout, input};
use std::*;

use num_integer::Integer;

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [i64;n],
    }

    let mut left = vec![0; n + 1];
    let mut right = vec![0; n + 1];

    for i in 0..n {
        left[i + 1] = left[i].gcd(&a[i]);
    }

    for i in (0..n).rev() {
        right[i] = right[i + 1].gcd(&a[i]);
    }

    let mut ans = 0;
    for i in 0..n {
        ans = ans.max(left[i].gcd(&right[i + 1]));
    }
    println!("{}", ans);
}
