use proconio::{fastout, input};
use std::collections::BTreeSet;

#[fastout]
fn main() {
    input! {n:usize,m:usize,aa:[usize;n],bb:[usize;m]}
    let mut bt: BTreeSet<(usize, usize)> = BTreeSet::new();

    for (i, a) in aa.iter().enumerate() {
        bt.insert((*a, i));
    }

    let mut ans = 0;

    for i in 0..m {
        let x = bt.range((bb[i], 0)..).cloned().next();
        if let Some(x) = x {
            ans += x.0;
            bt.remove(&x);
        } else {
            println!("-1");
            return;
        }
    }
    println!("{}", ans);
}
