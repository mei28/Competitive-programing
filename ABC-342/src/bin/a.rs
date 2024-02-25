use proconio::{fastout, input, marker::Chars};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        s: Chars,
    }

    let mut dict = HashMap::new();

    for i in s.iter() {
        *dict.entry(i).or_insert(0) += 1;
    }

    for (i, v) in s.iter().enumerate() {
        if dict.get(v).unwrap() == &1 {
            println!("{}", i + 1);
        }
    }
}
