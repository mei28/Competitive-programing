use proconio::{fastout, input, marker::*};
use std::cmp::{max, min};

#[fastout]
fn main() {
    input! {h:usize,w:usize,s: [Chars;h]}
    let mut dr = (0, 0);
    let mut ul = (h, w);

    for i in 0..h {
        for j in 0..w {
            if s[i][j] == '#' {
                dr.0 = std::cmp::max(dr.0, i);
                dr.1 = std::cmp::max(dr.1, j);

                ul.0 = std::cmp::min(ul.0, i);
                ul.1 = std::cmp::min(ul.1, j);
            }
        }
    }
    for i in ul.0..=dr.0 {
        for j in ul.1..=dr.1 {
            if s[i][j] == '.' {
                println!("{} {}", i + 1, j + 1);
                return;
            }
        }
    }
}
