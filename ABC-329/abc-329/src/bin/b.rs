use proconio::{fastout, input};
use std::collections::BTreeSet;

#[fastout]
fn main() {
    input! {n:usize,a:[usize;n]}
    let set = a.iter().collect::<BTreeSet<_>>();
    println!("{}", set.iter().rev().skip(1).next().unwrap())
}
