use proconio::{fastout, input, marker::Chars};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {n:usize,mut s:[Chars;n]}

    for i in 0..n {
        let t = s[i].iter().cloned().rev().collect::<Vec<_>>();
        s[i] = s[i].clone().min(t);
    }

    let mut hs = HashSet::new();

    for i in 0..n {
        hs.insert(s[i].clone());
    }

    println!("{}", hs.len());
}
