use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, a:[String;n]}

    let cnt = a.iter().filter(|s| **s == "Takahashi").count();
    println!("{}", cnt);
}
