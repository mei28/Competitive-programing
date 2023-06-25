use itertools::Itertools;
use proconio::{fastout, input, marker::Chars};

#[fastout]

fn main() {
    input! {n:usize, mut s:Chars}

    let mut accum = vec![0; n + 1];
    let mut stack = vec![];

    for i in 0..n {
        if s[i] == '(' {
            stack.push(i);
        } else if s[i] == ')' {
            if stack.len() > 0 {
                let j = stack.pop().unwrap();
                accum[j] += 1;
                accum[i + 1] -= 1;
            }
        }
    }

    for i in 0..n {
        accum[i + 1] += accum[i];
    }

    println!(
        "{}",
        (0..n).filter(|&i| accum[i] == 0).map(|i| s[i]).join("")
    );
}

