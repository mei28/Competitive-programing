use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,k:usize,aa:[usize;n]}

    let mut ans = 0;

    let mut sum = 0;
    for a in aa {
        if a + sum > k {
            ans += 1;
            sum = a;
        } else {
            sum += a;
        }
    }

    if sum > 0 {
        ans += 1;
    }
    println!("{}", ans);
}
