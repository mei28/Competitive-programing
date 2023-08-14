use proconio::{fastout, input};
use std::collections::BTreeMap;

#[fastout]
fn main() {
    input! {n:usize,mut ds:[usize;n],m:usize,mut ts:[usize;m]}
    ds.sort();
    ts.sort();

    if n < m {
        println!("NO");
        return;
    }
    let mut d_map = BTreeMap::new();
    let mut t_map = BTreeMap::new();

    for i in 0..n {
        d_map.entry(ds[i]).and_modify(|e| *e += 1).or_insert(1);
    }
    for i in 0..m {
        t_map.entry(ts[i]).and_modify(|e| *e += 1).or_insert(1);
    }

    for (k, v) in t_map.iter() {
        if *d_map.get(k).unwrap_or(&0) < *v {
            println!("NO");
            return;
        }
    }
    println!("YES");
}

