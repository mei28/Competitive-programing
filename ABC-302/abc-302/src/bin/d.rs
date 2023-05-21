use proconio::{fastout, input};
use std::collections::BTreeSet;

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        d: isize,
        a: [isize; n],
        b: [isize; m]
    }

    let bt = b.iter().copied().collect::<BTreeSet<_>>();
    let mut ans = -1;

    for x in a.iter() {
        if let Some(y) = bt.range(x - d..x + d).next() {
            if ans < x + y {
                ans = x + y;
            }
        }
        if let Some(y) = bt.range(x - d..=x + d).rev().next() {
            if ans < x + y {
                ans = x + y;
            }
        }
    }
    println!("{}", ans);
}
