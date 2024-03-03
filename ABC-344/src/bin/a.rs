use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {s: Chars}

    let left = (0..s.len()).find(|&i| s[i] == '|').unwrap();
    let right = (0..s.len()).rev().find(|&i| s[i] == '|').unwrap();

    let mut ans = vec![];
    for i in 0..left {
        ans.push(s[i])
    }
    for i in right + 1..s.len() {
        ans.push(s[i])
    }

    println!("{}", ans.into_iter().collect::<String>());
}
