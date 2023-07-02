use proconio::{fastout, input};
use std::collections::{HashMap, HashSet};

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        cs: [String; n],
        ds: [String; m],
        ps: [usize; m+1],
    }

    let mut dct: HashMap<String, usize> = HashMap::new();
    let cset: HashSet<_> = cs.iter().cloned().collect();
    let dset: HashSet<_> = ds.iter().cloned().collect();
    let pset = &cset - &dset;

    for (idx, d) in ds.iter().enumerate() {
        dct.insert(d.clone(), ps[idx + 1]);
    }

    for p in pset {
        dct.insert(p.clone(), ps[0]);
    }

    let mut ans = 0;
    for c in &cs {
        ans += dct.get(c).unwrap_or(&0);
    }
    println!("{}", ans);
}

