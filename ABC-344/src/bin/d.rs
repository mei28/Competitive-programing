use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        t: Chars,
        n: usize,
    }
    let mut a = vec![];
    let mut s = vec![];
    for _ in 0..n {
        input! {
            a_: usize,
            s_: [Chars; a_],
        }
        a.push(a_);
        s.push(s_);
    }

    let mut dp = vec![vec![1_usize << 60; t.len() + 1]; n + 1];
    dp[0][0] = 0;

    for i in 0..n {
        for j in 0..=t.len() {
            dp[i + 1][j] = dp[i][j];
        }
        for j in 0..a[i] {
            let s = &s[i][j];
            for k in 0..t.len() {
                let mut f = true;
                for l in 0..s.len() {
                    f &= k + l < t.len() && t[k + l] == s[l];
                }
                if f && dp[i + 1][k + s.len()] > dp[i][k] + 1 {
                    dp[i + 1][k + s.len()] = dp[i][k] + 1
                }
            }
        }
    }

    if dp[n][t.len()] == 1_usize << 60 {
        println!("-1");
    } else {
        println!("{}", dp[n][t.len()]);
    }
}

