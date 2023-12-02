use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:f64}
    let mut ans: f64 = 0.0;

    for i in 1..n as usize {
        ans += (n / i as f64);
    }
    println!("{}", ans);
}
