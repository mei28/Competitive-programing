use proconio::{fastout, input};
use std::cmp::min;

#[fastout]
fn main() {
    input! {n: usize, k: usize, a: [usize; n]}

    let mut pre = vec![0; k + 2];
    let mut suf = vec![0; k + 2];

    for i in 1..=k {
        pre[i] = pre[i - 1];
        if i % 2 == 0 {
            pre[i] += a[i - 1] - a[i - 2];
        }
    }

    for i in (0..k).rev() {
        suf[i] = suf[i + 1];
        if (k - i) % 2 == 0 {
            suf[i] += a[i + 1] - a[i];
        }
    }

    let mut ans = 1_000_000_000;

    for i in (0..=k).step_by(2) {
        ans = min(ans, pre[i] + suf[i]);
    }

    println!("{}", ans);
}

