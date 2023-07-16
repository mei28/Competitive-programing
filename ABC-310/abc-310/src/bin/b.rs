use proconio::{fastout, input};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {n:usize,_m:usize,}
    let mut pf = vec![];

    for _ in 0..n {
        input! {
            p:usize,c:usize,f:[usize;c]
        }
        pf.push((p, f.into_iter().collect::<HashSet<_>>()));
    }

    for i in 0..n {
        for j in 0..n {
            if i == j {
                continue;
            }

            if pf[i].0 >= pf[j].0 && pf[i].1.is_subset(&pf[j].1) {
                if pf[i].0 > pf[j].0 || pf[i].1.len() < pf[j].1.len() {
                    println!("Yes");
                    return;
                }
            }
        }
    }
    println!("No");
}
