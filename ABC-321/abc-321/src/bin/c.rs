use proconio::{fastout, input};
use std::collections::HashSet;

fn dfs(a: &mut Vec<usize>, cands: &mut HashSet<usize>, k: usize) {
    if cands.len() > k {
        return;
    } else {
        for i in 0..=9 {
            if a[a.len() - 1] <= i {
                continue;
            }
            a.push(i);
            cands.insert(a.iter().fold(0, |acc, x| acc * 10 + x));
            dfs(a, cands, k);
            a.pop();
        }
        return;
    }
}

#[fastout]
fn main() {
    input! {k:usize}
    let mut cands = HashSet::new();

    for i in 1..=9 {
        cands.insert(i);
    }

    for i in 0..=9 {
        dfs(&mut vec![i], &mut cands, k*10);
    }

    let mut ans: Vec<usize> = cands.into_iter().collect();
    ans.sort();
    println!("{}", ans[k-1]);
}
