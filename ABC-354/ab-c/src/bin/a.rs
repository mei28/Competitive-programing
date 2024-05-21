use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {h:i32}
    let mut ans = 0;
    let mut a = 0;

    while a <= h {
        a += 2_i32.pow(ans);
        ans += 1;
    }
    println!("{}", ans);
}
