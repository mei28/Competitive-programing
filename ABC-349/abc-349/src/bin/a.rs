use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, aa:[i32;n-1]}

    println!("{}", -aa.iter().sum::<i32>());
}
