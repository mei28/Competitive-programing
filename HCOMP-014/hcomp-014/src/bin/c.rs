use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
    }

    if n % 2 != 0 {
        println!("{}", 0);
        return;
    }

    let mut ans: usize = n / 10;
    let n = n / 10;

    let mut five = 5;
    while five <= n {
        ans += n / five;
        five = five * 5;
    }
    println!("{}", ans);
}
