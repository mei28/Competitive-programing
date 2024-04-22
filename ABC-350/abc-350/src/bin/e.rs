use proconio::input;
use std::collections::HashMap;

fn solve(n: u64, a: u64, x: u64, y: u64, memo: &mut HashMap<(u64, u64, u64, u64), f64>) -> f64 {
    if let Some(&ans) = memo.get(&(n, a, x, y)) {
        return ans;
    }

    if n == 0 {
        return 0.0;
    }

    let ans0 = solve(n / a, a, x, y, memo) + x as f64;
    let ans1 =
        (2..=6).map(|i| solve(n / i, a, x, y, memo)).sum::<f64>() / 5.0 + y as f64 * 6.0 / 5.0;
    let ans = ans0.min(ans1);
    memo.insert((n, a, x, y), ans);
    ans
}

fn main() {
    input! {
        n:u64,
        a:u64,
        x:u64,
        y:u64,
    }

    let mut memo: HashMap<(u64, u64, u64, u64), f64> = HashMap::new();
    let ans = solve(n, a, x, y, &mut memo);
    println!("{}", ans);
}
