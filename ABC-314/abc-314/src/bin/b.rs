use itertools::Itertools;
use proconio::{fastout, input};
use std::collections::BTreeSet;

#[fastout]
fn main() {
    input! {n:usize}
    let mut a = vec![];

    for _ in 0..n {
        input! {c:usize,v:[usize;c],}
        a.push(v.into_iter().collect::<BTreeSet<_>>());
    }

    input! {x:usize}

    if (0..n).all(|i| !a[i].contains(&x)) {
        println!("0");
        return;
    }

    let m = (0..n)
        .filter(|i| a[*i].contains(&x))
        .map(|i| a[i].len())
        .min()
        .unwrap();

    let ans = (0..n)
        .filter(|i| a[*i].contains(&x) && a[*i].len() == m)
        .collect::<Vec<_>>();

    println!("{}", ans.len());
    println!("{}", ans.iter().map(|x| x + 1).join(" "));
}
