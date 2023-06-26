use proconio::{fastout, input};

const MOD: i32 = 1000000007;

#[fastout]
fn main() {
    input! {n:usize,m:usize, a:[usize;m]}
    let mut is_a = vec![true; n + 10];
    let mut dp = vec![0; n + 10];

    for i in 0..m {
        is_a[a[i]] = false;
    }

    dp[0] = 1;

    for i in 1..=n {
        if !is_a[i] {
            dp[i] = 0;
            continue;
        }
        if i == 1 {
            dp[i] += dp[i - 1];
        } else {
            dp[i] += dp[i - 1] + dp[i - 2];
        }
        dp[i] %= MOD;
    }

    println!("{}", dp[n]);
}
