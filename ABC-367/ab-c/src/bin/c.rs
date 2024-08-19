use itertools::Itertools;
use proconio::input;

fn dfs(index: usize, current_sum: i32, sequence: &mut Vec<i32>, n: usize, k: i32, r: &[i32]) {
    if index == n {
        if current_sum % k == 0 {
            println!("{}", sequence.iter().map(|x| x.to_string()).join(" "));
        }
        return;
    }

    for i in 1..=r[index] {
        sequence.push(i);
        dfs(index + 1, current_sum + i, sequence, n, k, r);
        sequence.pop();
    }
}

fn main() {
    input! {
        n: usize,
        k: i32,
        r: [i32; n],
    }

    let mut sequence = Vec::new();
    dfs(0, 0, &mut sequence, n, k, &r);
}
