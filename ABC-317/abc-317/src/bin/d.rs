use proconio::{fastout, input};
use std::cmp::{max, min};

const INF: i64 = 1e18 as i64;

#[fastout]
fn main() {
    input! {
        n: usize,
        xyz: [(i64, i64, i64); n]  // Using i64 here to match long long in C++
    }

    let z_sum = xyz.iter().map(|(_, _, z)| *z as usize).sum::<usize>();
    let mut dp = vec![INF; z_sum + 1];

    dp[0] = 0;

    for &(x, y, z) in &xyz {
        // Directly destructure tuple here
        let w = max(0, (x + y) / 2 + 1 - x);

        for j in (z as usize..=z_sum).rev() {
            dp[j] = min(dp[j], dp[j - z as usize] + w);
        }
    }

    let mut ans = INF;
    for j in (z_sum / 2 + 1)..=z_sum {
        ans = min(ans, dp[j]);
    }
    println!("{}", ans);
}

