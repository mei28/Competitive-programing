use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,l:usize,r:usize}

    let mut ans = Vec::new();
    ans.extend(1..l);
    ans.extend((l..=r).rev());
    ans.extend(r + 1..=n);
    println!("{}", ans.iter().join(" "));
}
