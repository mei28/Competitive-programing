use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {s:String}
    println!("{}", s.split(".").collect::<Vec<_>>().last().unwrap());
}
