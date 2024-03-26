use proconio::{fastout, input};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
        n: usize,
        a: usize,
        b: usize,
        ds: [usize; n]
    }
    let mut dds: Vec<usize> = ds
        .iter()
        .map(|d| d % (a + b))
        .collect::<HashSet<usize>>() // HashSet<usize>の生成
        .into_iter() // HashSetからVecへ変換
        .collect();
    dds.sort(); // Vecをソート

    let is_possible = (0..dds.len().saturating_sub(1)) // アンダーフローを防ぐ
        .map(|i| (dds[i + 1] - dds[i]) % (a + b))
        .any(|d| d >= b);
    if !is_possible {
        println!("Yes");
    } else {
        println!("No");
    }
}
