use proconio::input;
use std::cmp::min;

fn main() {
    input! {
        n: usize,
        k: usize,
        p: usize,
        data: [[usize; k + 1]; n],
    }

    let half = n / 2;

    let mut first_half = Vec::new();

    for i in 0..(1 << half) {
        let mut sum = vec![0; k];
        let mut cost = 0;
        for j in 0..half {
            if (i >> j) & 1 == 1 {
                cost += data[j][0];
                for l in 0..k {
                    sum[l] += data[j][l + 1];
                }
            }
        }
        first_half.push((sum, cost));
    }

    let mut ans = std::usize::MAX;

    for i in 0..(1 << (n - half)) {
        let mut sum = vec![0; k];
        let mut cost = 0;
        for j in 0..(n - half) {
            if (i >> j) & 1 == 1 {
                cost += data[half + j][0];
                for l in 0..k {
                    sum[l] += data[half + j][l + 1];
                }
            }
        }
        for (f_sum, f_cost) in &first_half {
            if sum.iter().zip(f_sum.iter()).all(|(s, f_s)| s + f_s >= p) {
                ans = min(ans, cost + f_cost);
            }
        }
    }

    if ans == std::usize::MAX {
        println!("-1");
    } else {
        println!("{}", ans);
    }
}

