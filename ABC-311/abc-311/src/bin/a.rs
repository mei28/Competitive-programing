use std::collections::HashSet;

use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {n:usize, s:Chars}

    let mut hs = HashSet::new();

    for i in 0..n {
        hs.insert(s[i]);
        if hs.len() == 3 {
            println!("{}", i + 1);
            return;
        }
    }
}
