use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        n: usize,
        sc: [(usize, usize); n]
    }
    let mut hs: HashMap<usize, usize> = HashMap::new();

    for (s, c) in sc {
        let mut f = s;

        while f % 2 == 0 {
            f /= 2;
        }
        *hs.entry(f).or_insert(0) += (s / f) * c;
    }

    let mut ans = 0;
    for (_, v) in hs {
        ans += v.count_ones();
    }
    println!("{}", ans);
}
