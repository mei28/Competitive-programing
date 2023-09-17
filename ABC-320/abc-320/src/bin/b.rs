use proconio::{fastout, input, marker::Chars};
use std::cmp::max;

#[fastout]
fn main() {
    input! {s:Chars}

    let n = s.len();
    let mut ans = 1;
    for i in 0..n {
        for j in i + 1..=n {
            let mut a = vec![];
            for k in i..j {
                a.push(s[k]);
            }
            let b = a.iter().rev().cloned().collect::<Vec<_>>();

            if a == b {
                ans = max(ans, a.len());
            }
        }
    }
    println!("{}", ans);
}
