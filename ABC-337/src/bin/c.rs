use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {mut n:isize, mut aa: [isize;n]}
    aa.insert(0, 0);
    let mut hs = HashMap::new();
    let mut idx = -1;

    for i in 1..=n {
        hs.insert(aa[i as usize], i);
    }

    let mut ans = vec![];

    while n > 0 {
        idx = *hs.get(&idx).unwrap();
        ans.push(idx);
        n -= 1;
    }
    let ans_str = ans
        .iter()
        .map(|&num| num.to_string())
        .collect::<Vec<String>>()
        .join(" ");
    println!("{}", ans_str);
}
