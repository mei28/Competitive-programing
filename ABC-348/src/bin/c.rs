use proconio::{fastout, input};
use std::cmp::max;
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {n:usize,ac:[(usize,usize);n]}

    let mut map = HashMap::new();
    for (c, a) in ac {
        let count = map.entry(a).or_insert(std::usize::MAX);
        if *count > c {
            *count = c;
        }
    }

    let mut ans = 0;
    for (k, v) in map.iter() {
        ans = max(ans, *v);
    }
    println!("{}", ans);
}
