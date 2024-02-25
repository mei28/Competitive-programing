use proconio::{fastout, input};
use std::collections::HashMap;

fn f(v: usize, map: &mut HashMap<usize, usize>) -> usize {
    if v == 1 {
        return 0;
    }
    if map.contains_key(&v) {
        return map[&v];
    }

    let first_half = f(v / 2, map); // 最初の関数呼び出しの結果を保存
    let second_half = f((v + 1) / 2, map); // 2番目の関数呼び出しの結果を保存
    map.insert(v, first_half + second_half + v); // mapに値を挿入
    return map[&v];
}
#[fastout]
fn main() {
    input! {n:usize}

    let mut map = HashMap::new();
    println!("{}", f(n, &mut map));
}
