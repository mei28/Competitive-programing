use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, a:[usize;n]}
    let ans = a.iter().sum::<usize>() - n;
    println!("{}", ans);
}
