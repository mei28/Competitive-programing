use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {n:usize, aa:[usize;n]}

    let mut map: HashMap<usize, usize> = HashMap::new();
    let mut zero_cnt = 0;

    for a in aa {
        if a == 0 {
            zero_cnt += 1;
            continue;
        }
        let d = largest_square_divisor(a);
        *map.entry(d).or_insert(0) += 1;
    }

    let mut ans = zero_cnt * (zero_cnt - 1) / 2; // 0のペアの数

    for (_, v) in map {
        ans += v * (v - 1) / 2; // 同じdを持つ数のペアの数
    }

    println!("{}", ans);
}

// aを割り切る最大の平方数を求める関数
fn largest_square_divisor(mut a: usize) -> usize {
    let mut divisor = 1;
    for i in 2..=(a as f64).sqrt() as usize + 1 {
        let mut count = 0;
        while a % i == 0 {
            a /= i;
            count += 1;
        }
        if count % 2 == 1 {
            divisor *= i;
        }
    }
    if a > 1 {
        // aが1より大きい場合、a自体が素数
        divisor *= a;
    }
    divisor
}

