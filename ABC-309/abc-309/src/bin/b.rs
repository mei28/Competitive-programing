use itertools::Itertools;
use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        n: usize,
        a: [Chars; n],
    }

    let mut b = a.clone();
    for i in 0..n {
        for j in 0..n {
            if i == 0 && 0 < j {
                b[i][j] = a[i][j - 1];
            } else if j == n - 1 && i > 0 {
                b[i][j] = a[i - 1][j];
            } else if i == n - 1 && j < n - 1 {
                b[i][j] = a[i][j + 1];
            } else if j == 0 && i < n - 1 {
                b[i][j] = a[i + 1][j];
            }
        }
    }

    for r in b {
        println!("{}", r.iter().join(""));
    }
}

