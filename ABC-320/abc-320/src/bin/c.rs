use proconio::{fastout, input, marker::Chars};
use std::cmp::{max, min};

#[fastout]
fn main() {
    input! {m:usize,ss: [Chars;3]}
    let mut ans = std::usize::MAX;
    for i in 0..3 * m {
        for j in 0..3 * m {
            for k in 0..3 * m {
                let a = ss[0][i % m];
                let b = ss[1][j % m];
                let c = ss[2][k % m];

                if a == b && b == c && a == c {
                    if i != j && j != k && i != k {
                        ans = min(ans, *[i, j, k].iter().max().unwrap());
                    }
                }
            }
        }
    }
    if ans != std::usize::MAX {
        print!("{}", ans);
    } else {
        print!("{}", -1);
    }
}
