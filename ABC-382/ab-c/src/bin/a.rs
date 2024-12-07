use proconio::{input, marker::Chars};
use std::cmp::min;

fn main() {
    input! {n:usize,d:usize,ss:Chars}

    let cnt_at = ss.iter().filter(|&&c| c == '@').count();
    let cnt_dot = ss.iter().filter(|&&c| c == '.').count();

    print!("{}", cnt_dot + min(cnt_at, d));
}
