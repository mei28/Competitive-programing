use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        xy: [(u64, i64); n]
    }

    let mut dp = vec![vec![-4e18 as i64; 2]; n + 1];
    dp[0][0] = 0;

    for i in 0..n {
        if xy[i].0 == 0 {
            dp[i + 1][0] = dp[i][0].max((dp[i][0].max(dp[i][1])) + xy[i].1);
        } else {
            dp[i + 1][1] = dp[i][1].max(dp[i][0] + xy[i].1);
        }

        dp[i + 1][0] = dp[i + 1][0].max(dp[i][0]);
        dp[i + 1][1] = dp[i + 1][1].max(dp[i][1]);
    }
    println!("{}", dp[n][0].max(dp[n][1]));
}

