use proconio::{fastout, input};
use std::usize::MAX;

#[fastout]
fn main() {
    input! {
        n: usize,
        k: usize,
        mut aa: [usize; n],
    }
    aa.sort();
    let mut ans = MAX;

    for i in 0..=k {
        ans = ans.min(aa[i+(n-k)-1] - aa[i]);
    }

    println!("{}", ans);
}
