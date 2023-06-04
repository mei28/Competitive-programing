use itertools::Itertools;
use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {mut s:Chars}

    for i in 3..s.len() {
        s[i] = '0';
    }

    println!("{}", s.iter().join(""));
}
