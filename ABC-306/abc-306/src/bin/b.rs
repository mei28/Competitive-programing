use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {a:[u128;64]}
    let mut ans: u128 = 0;
    let mut base: u128 = 1;

    for b in a {
        ans += base * b;
        base *= 2;
    }
    println!("{}", ans);
}
