use proconio::{fastout, input, marker::Chars};
use std::collections::HashMap;

fn fact(n: usize) -> usize {
    match n {
        0 => 1,
        1 => 1,
        _ => n * fact(n - 1),
    }
}

#[fastout]
fn main() {
    input! {s:Chars}
    let n = s.len();
    let mut map = HashMap::new();

    for c in s.iter() {
        let count = map.entry(*c).or_insert(0);
        *count += 1;
    }

    let mut ans = (n * n - map.values().fold(0, |acc, x| acc + x * x)) / 2;
    if map.values().max().unwrap() > &1 {
        ans += 1;
    }
    println!("{}", ans)
}
