use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {a:usize,b:usize,d:usize}
    let ans = (a..=b).step_by(d).collect::<Vec<usize>>();
    println!("{}", ans.iter().join(" "));
}
