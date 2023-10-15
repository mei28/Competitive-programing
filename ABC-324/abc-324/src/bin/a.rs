use proconio::{fastout, input};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {n:usize, a:[usize;n]}

    let mut hs: HashSet<usize> = HashSet::new();
    for i in a.iter() {
        hs.insert(*i);
    }

    if hs.len() == 1 {
        println!("Yes")
    } else {
        println!("No")
    }
}
