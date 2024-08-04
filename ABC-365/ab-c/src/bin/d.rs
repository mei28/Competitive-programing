use proconio::input;

fn main() {
    input! {
        n: usize,
        s: String,
    }

    let s: Vec<char> = s.chars().collect();
    let mut dp = vec![[0; 3]; n + 1];

    for i in 0..n {
        let current_hand = s[i];
        for prev_hand in 0..3 {
            match current_hand {
                'R' => {
                    if prev_hand != 1 {
                        dp[i + 1][1] = dp[i + 1][1].max(dp[i][prev_hand] + 1);
                    }
                    if prev_hand != 0 {
                        dp[i + 1][0] = dp[i + 1][0].max(dp[i][prev_hand]);
                    }
                }
                'P' => {
                    if prev_hand != 2 {
                        dp[i + 1][2] = dp[i + 1][2].max(dp[i][prev_hand] + 1);
                    }
                    if prev_hand != 1 {
                        dp[i + 1][1] = dp[i + 1][1].max(dp[i][prev_hand]);
                    }
                }
                'S' => {
                    if prev_hand != 0 {
                        dp[i + 1][0] = dp[i + 1][0].max(dp[i][prev_hand] + 1);
                    }
                    if prev_hand != 2 {
                        dp[i + 1][2] = dp[i + 1][2].max(dp[i][prev_hand]);
                    }
                }
                _ => unreachable!(),
            }
        }
    }

    let result = dp[n][0].max(dp[n][1]).max(dp[n][2]);
    println!("{}", result);
}
