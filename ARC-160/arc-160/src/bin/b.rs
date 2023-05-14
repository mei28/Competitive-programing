// use cmp::{max, min, Reverse};
use proconio::{fastout, input, marker::*};
use std::*;

const MOD: usize = 998244353;

fn solve(n: usize) -> usize {
    let mut count = vec![0; n+1];

    for i in 1..=n {
        for j in i..=n {
            count[j] += 1;
        }
    }
    let mut ans: usize = 0;
    for i in 1..=n {
        ans += count[i] * count[i] * count[i];
        ans %= MOD;
    }
    return ans;
}

#[fastout]
fn main() {
    input! {
        n: usize,
    }

    for _ in 0..n {
        input! {
            t: usize,
        }
        println!("{}", solve(t));
    }
}
