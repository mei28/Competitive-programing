use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, s:[usize;n]}
    let mut dp = vec![0; (100 * 100 + 10)];
    dp[0] = 1;

    for i in 0..n {
        for j in (0..100 * 100 + 10).rev() {
            if dp[j] == 1 {
                dp[j + s[i]] = 1
            }
        }
    }

    let mut ans = 0;
    for i in 0..100 * 100 + 10 {
        if (dp[i] == 1) && (i % 10 != 0) {
            ans = i;
        }
    }
    println!("{}", ans);
}
