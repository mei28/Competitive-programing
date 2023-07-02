use proconio::{fastout, input};
use std::cmp::Ordering;

#[fastout]
fn main() {
    input! {
        n: usize,
        ab: [(i64, i64); n],
    }

    let mut rates: Vec<_> = ab
        .into_iter()
        .enumerate()
        .map(|(i, (a, b))| ((a, a + b), i))
        .collect();

    rates.sort_unstable_by(|a, b| {
        let ((a1, b1), i) = a;
        let ((a2, b2), j) = b;
        match a1 * b2 == a2 * b1 {
            true => i.cmp(j),
            false => (a2 * b1).cmp(&(a1 * b2)),
        }
    });

    for rate in rates {
        print!("{} ", rate.1 + 1);
    }
    println!();
}

