use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {n:usize,a:[usize;3*n]}

    let mut hmap: HashMap<usize, Vec<usize>> = HashMap::new();

    for (i, b) in a.iter().enumerate() {
        hmap.entry(*b).or_insert(vec![]).push(i + 1);
    }

    let mut ans = vec![];

    for k in hmap.keys().cloned() {
        let mut val = hmap.get(&k).unwrap().clone();
        val.sort();
        ans.push((k, val[1])); // take the middle value (index 1)
    }

    ans.sort_by(|a, b| a.1.cmp(&b.1));
    for a in ans {
        println!("{}", a.0);
    }
}

