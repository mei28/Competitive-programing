use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
    s:String
    }
    let ans = s.clone().to_uppercase();
    println!("{}", ans);
}
