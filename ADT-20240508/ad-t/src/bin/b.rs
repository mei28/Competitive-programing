use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:u32}
    println!("{}", (2 as i64).pow(n));
}
