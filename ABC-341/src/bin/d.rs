use proconio::{fastout, input};
use std::cmp::max;

fn gcd(a: usize, b: usize) -> usize {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn lcm(a: usize, b: usize) -> usize {
    a / gcd(a, b) * b
}

#[fastout]
fn main() {
    input! {n:usize,m:usize,k:usize}

    let mut ng = 0;
    let mut ok = max(n, m) * (k + 10);
    let l = lcm(n, m);

    while ok - ng > 1 {
        let mid = (ok + ng) / 2;

        let cnt = (mid / n) + (mid / m) - 2*(mid / l);

        if cnt < k {
            ng = mid;
        } else {
            ok = mid;
        }
    }
    println!("{}", ok);
}
