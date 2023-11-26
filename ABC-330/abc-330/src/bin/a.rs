use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,l:usize,a:[usize;n]}
    let ans = a.into_iter().filter(|x| *x >= l).count();
    println!("{}", ans)
}
