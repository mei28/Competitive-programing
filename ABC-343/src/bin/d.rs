use proconio::{fastout, input};
use std::collections::{HashMap, HashSet};

#[fastout]
fn main() {
    input! {n:usize,t:usize}

    let mut map = HashMap::new();
    for i in 1..=n {
        map.entry(i).or_insert(0);
    }
    for _ in 0..t {
        input! {a:usize,b:usize}
        *map.entry(a).or_insert(0) += b;
        let set: HashSet<usize> = HashSet::from_iter(map.values().cloned());
        println!("{}", set.len());
    }
}
