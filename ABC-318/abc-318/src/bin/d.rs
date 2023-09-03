use itertools::Itertools;
use proconio::{fastout, input, marker::*};
use std::cmp::max;

fn main() {
    input! {
        n: usize,
    }

    let mut d = vec![vec![0; n]; n];

    for i in 0..n - 1 {
        input! {e:[usize;n-1-i]};
        for j in 0..e.len() {
            d[i][i + j + 1] = e[j];
            d[i + j + 1][i] = e[j];
        }
    }
    let mut max_val = 0;
    for comb in (0..n).combinations(if n % 2 == 1 { n - 1 } else { n }) {
        let mut dp = vec![-1; 1 << comb.len()];
        dp[0] = 0 as isize;

        for s in 0..(1 << comb.len()) {
            for i in 0..comb.len() {
                for j in (i + 1)..comb.len() {
                    if (s & (1 << i) == 0) && (s & (1 << j) == 0) {
                        let next_state = s | (1 << i) | (1 << j);
                        dp[next_state] = max(dp[next_state], dp[s] + d[comb[i]][comb[j]] as isize);
                    }
                }
            }
        }

        max_val = max(max_val, dp[(1 << comb.len()) - 1]);
    }
    println!("{}", max_val);
}
