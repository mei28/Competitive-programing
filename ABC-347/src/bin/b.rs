use proconio::{fastout, input, marker::*};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {s: Chars}

    let mut set = HashSet::new();
    for i in 0..s.len() {
        for j in 0..s.len() {
            if i + j > s.len() {
                break;
            }
            let c = s[i..i + j].iter().collect::<String>();
            set.insert(c);
        }
    }
    println!("{}", set.len());
}
