use itertools::Itertools;
use proconio::{input, marker::Chars};

fn main() {
    input! {s: Chars}
    let mut ans = "UPC".to_string();

    println!("{}", s[0].to_string() + &ans);
}
