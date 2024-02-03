use proconio::input;
use std::cmp::{max, min};

fn main() {
    input! {n:usize, mut a:[usize;n]}
    a.insert(0, 0);

    let mut l = vec![0; n + 2];
    let mut r = vec![0; n + 2];

    for i in 1..=n {
        l[i] = min(a[i], l[i - 1] + 1);
    }

    for i in (0..=n).rev() {
        r[i] = min(a[i], r[i + 1] + 1);
    }
    println!(
        "{}",
        l.iter().zip(r.iter()).map(|(x, y)| x.min(y)).max().unwrap(),
    )
}
