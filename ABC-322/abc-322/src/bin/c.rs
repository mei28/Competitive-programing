use proconio::{fastout, input};
use std::collections::BTreeSet;

#[fastout]
fn main() {
    input! { n:usize,m:usize,a:[usize;m] }

    let set = a.into_iter().collect::<BTreeSet<usize>>();

    for i in 1..=n {
        println!("{}", set.range(i..).next().unwrap() - i);
    }
}
