use proconio::{fastout, input};
use std::collections::BTreeSet;

#[fastout]
fn main() {
    input! {
        _n: usize,
        q: usize,
    }

    let mut set = BTreeSet::new();
    let mut cnt = 0;

    for _ in 0..q {
        input! {
            t:usize,
        }

        if t == 1 {
            cnt += 1;
            set.insert(cnt);
        } else if t == 2 {
            input! {x:usize}
            set.remove(&x);
        } else {
            println!("{}", set.iter().next().unwrap());
        }
    }
}
