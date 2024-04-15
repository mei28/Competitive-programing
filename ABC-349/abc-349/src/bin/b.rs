use std::collections::{HashMap, HashSet};

use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {s: Chars}
    let mut cnt_1 = HashMap::new();
    let mut cnt_2 = HashMap::new();

    for c in s.iter() {
        *cnt_1.entry(c).or_insert(0) += 1;
    }

    for (k, v) in cnt_1.iter() {
        let tmp = cnt_2.entry(v).or_insert(HashSet::new());
        tmp.insert(k);
    }

    for (k, v) in cnt_2.iter() {
        if v.len() != 0 && v.len() != 2 {
            println!("No");
            return;
        }
    }
    println!("Yes");
}
