use proconio::{fastout, input, marker::Chars};
use std::cmp::{max, min};

#[fastout]
fn main() {
    input! {p:Chars,q:Chars};

    // convert chart to int
    // e.g. A->0, B->1
    let left = p[0] as usize - 'A' as usize;
    let right = q[0] as usize - 'A' as usize;

    let v = [0, 3, 4, 8, 9, 14, 23];
    println!("{}", v[max(left, right)] - v[min(left, right)]);
}
