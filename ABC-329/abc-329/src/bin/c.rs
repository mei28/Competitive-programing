use proconio::{fastout, input, marker::Chars};
use std::collections::HashMap;

fn rl(s: &[char]) -> usize {
    let mut total_count = 0;
    let mut current_count = 1;
    let mut prev_char = '\0';
    let mut hm = HashMap::new();

    for &c in s {
        if c == prev_char {
            current_count += 1;
        } else {
            if prev_char != '\0' {
                let entry = hm.entry(prev_char).or_insert(0);
                *entry = (*entry).max(current_count);
            }
            prev_char = c;
            current_count = 1;
        }
    }
    let entry = hm.entry(prev_char).or_insert(0);
    *entry = (*entry).max(current_count);
    for &count in hm.values() {
        total_count += count;
    }

    total_count
}

#[fastout]
fn main() {
    input! {
        n: usize,
        s: Chars,
    }
    let result = rl(&s);
    println!("{}", result);
}
