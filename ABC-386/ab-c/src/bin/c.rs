use proconio::input;

fn leveinshetin_distance(a: &str, b: &str) -> usize {
    let a_bytes = a.as_bytes();
    let b_bytes = b.as_bytes();

    let len_a = a.len();
    let len_b = b.len();

    let mut dp = vec![vec![0; len_b + 1]; len_a + 1];

    for i in 0..=len_a {
        dp[i][0] = i;
    }
    for j in 0..=len_b {
        dp[0][j] = j;
    }

    for i in 1..=len_a {
        for j in 1..=len_b {
            let cost = if a_bytes[i - 1] == b_bytes[j - 1] {
                0
            } else {
                1
            };

            dp[i][j] = std::cmp::min(
                dp[i - 1][j] + 1,
                std::cmp::min(dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost),
            );
        }
    }

    dp[len_a][len_b]
}
fn main() {
    input! {
        k: usize,
        a: String,
        b: String,
    }

    let discance = leveinshetin_distance(&a, &b);
    if discance <= k {
        println!("Yes")
    } else {
        println!("No")
    }
}
