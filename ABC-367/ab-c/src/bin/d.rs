use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {
        n: usize,
        m: i64,
        a: [i64; n],
    }

    let mut cumulative_sum = vec![0; 2 * n + 1];
    for i in 0..2 * n {
        cumulative_sum[i + 1] = cumulative_sum[i] + a[i % n];
    }

    let mut count_map = HashMap::new();
    let mut result = 0;

    for i in 0..=2 * n {
        let mod_value = cumulative_sum[i] % m;
        if let Some(&count) = count_map.get(&mod_value) {
            if i >= n {
                result += count;
            }
        }
        *count_map.entry(mod_value).or_insert(0) += 1;
    }

    println!("{}", result);
}
