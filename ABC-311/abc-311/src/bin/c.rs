use proconio::{fastout, input, marker::Usize1};
use std::collections::HashSet;
use itertools::Itertools;

#[fastout]
fn main() {
    input! {n:usize, a:[Usize1;n],}

    let mut h = vec![];
    let mut now = 0;
    h.push(now);

    let mut set = HashSet::new();
    set.insert(now);

    loop {
        now = a[now];
        if set.contains(&now) {
            let mut ans = vec![];
            while let Some(x) = h.pop() {
                ans.push(x);
                if x == now {
                    ans.reverse();
                    println!("{}", ans.len());
                    println!("{}", ans.into_iter().map(|x| x + 1).join(" "));
                    return;
                }
            }
        } else {
            h.push(now);
            set.insert(now);
        }
    }
}
