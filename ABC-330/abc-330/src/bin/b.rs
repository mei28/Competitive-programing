use proconio::{fastout, input};
use std::cmp::{max, min};

#[fastout]
fn main() {
    input! {n:usize,l:usize,r:usize,a:[usize;n]}

    for i in 0..n {
        let b = a[i];
        if l <= b && b <= r {
            print!("{} ", b);
            continue;
        } else if b < l {
            print!("{} ", l);
        } else {
            print!("{} ", r);
        }
    }
}
