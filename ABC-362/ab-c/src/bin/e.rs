use proconio::input;
use std::collections::HashMap;

fn count_arithmetic_subsequences(N: usize, A: Vec<i64>) -> Vec<i64> {
    const MOD: i64 = 998244353;
    let mut results = vec![0; N];
    let mut dp = vec![HashMap::new(); N];

    for i in 0..N {
        for j in 0..i {
            let diff = A[i] - A[j];
            let count = dp[j].get(&diff).copied().unwrap_or(0);
            let entry = dp[i].entry(diff).or_insert(0);
            *entry = (*entry + count + 1) % MOD;
            results[1] = (results[1] + 1) % MOD; 
            if count > 0 {
                results[2] = (results[2] + count) % MOD; 
            }
        }
    }

    for i in 3..=N {
        results[i - 1] = 0;
    }

    results
}

fn main() {
    input! {
        N: usize,
        A: [i64; N],
    }

    let results = count_arithmetic_subsequences(N, A);

    for (i, result) in results.iter().enumerate() {
        if i > 0 {
            print!(" ");
        }
        print!("{}", result);
    }
    println!();
}

