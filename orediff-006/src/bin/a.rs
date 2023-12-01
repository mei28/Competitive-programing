use itertools::Itertools;
use proconio::{fastout, input};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {h:usize, w:usize, aa:[[usize; w]; h]}

    let mut ans = 0;

    let n = h + w - 2;

    for bits in 0..1 << n {
        let mut hc = 0;
        let mut wc = 0;
        let mut v = vec![];
        let mut s = HashSet::new();
        for j in 0..n {
            if (bits >> j) & 1 == 1 {
                v.push(0);
                hc += 1;
            } else {
                v.push(1);
                wc += 1
            }
        }

        if hc == h - 1 && wc == w - 1 {
            let mut x = 0;
            let mut y = 0;
            s.insert(aa[x][y]);
            for i in 0..n {
                if v[i] == 0 {
                    x += 1;
                } else {
                    y += 1;
                }
                s.insert(aa[x][y]);
            }
        }

        if s.len() == n + 1 {
            ans += 1;
        }
    }
    println!("{}", ans);
}
