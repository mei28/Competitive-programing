use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {n:usize, sc: [(String,usize);n]}
    let sum = sc.iter().map(|(_, c)| c).sum::<usize>();

    let mut s: Vec<String> = sc.iter().map(|(s, _)| s.clone()).collect();
    s.sort();
    let map = s
        .iter()
        .enumerate()
        .map(|(i, s)| (i, s.clone()))
        .collect::<HashMap<usize, String>>();
    println!("{}", map.get(&(sum % n)).unwrap());
}
