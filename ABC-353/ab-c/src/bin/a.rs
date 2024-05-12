use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,hs:[usize;n]}

    let idx = hs.iter().enumerate().filter(|(i, &a)| a > hs[0]).next();
    println!("{}", idx.map(|(i, _)| (i + 1) as isize).unwrap_or(-1));
}
