use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:isize}
    let ans = if n > 0 { (n + 10 - 1) / 10 } else { -(-n) / 10 };
    println!("{}", ans);
}
