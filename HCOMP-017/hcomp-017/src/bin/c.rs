use proconio::{fastout, input};
use std::cmp::min;
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {n :usize, v:[usize; n]}

    let mut cnt = [HashMap::new(), HashMap::new()];

    for i in 0..n {
        *cnt[i % 2].entry(v[i]).or_insert(0) += 1;
    }

    let mut vv = vec![vec![]; 2];

    for i in 0..2 {
        for (key, val) in &cnt[i] {
            vv[i].push((*val, *key));
        }
        vv[i].sort_by(|a, b| b.0.cmp(&a.0));
    }
    
    if vv[0][0].1 != vv[1][0].1 {
        let ans = n - vv[0][0].0 - vv[1][0].0;
        println!("{}", ans);
        return;
    }

    if vv[0].len() == 1 && vv[1].len() == 1 {
        let ans = n / 2;
        println!("{}", ans);
        return;
    }

    let mut ans = std::usize::MAX;
    if vv[0].len() >= 2 {
        ans = min(ans, n - vv[0][1].0 - vv[1][0].0);
    }
    if vv[1].len() >= 2 {
        ans = min(ans, n - vv[0][0].0 - vv[1][1].0);
    }
    println!("{}", ans);
}
