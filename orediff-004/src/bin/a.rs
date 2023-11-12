use proconio::{fastout, input};
use std::cmp::{max, min};

#[fastout]
fn main() {
    input! {a:usize, b:usize,mut w:usize}
    w *= 1000;
    let mut mi = 1 << 32;
    let mut ma = 0;
    for i in 0..100000 {
        if a * i <= w && w <= b * i {
            mi = min(mi, i);
            ma = max(ma, i);
        }
    }

    if ma == 0 {
        println!("UNSATISFIABLE");
    } else {
        println!("{} {}", mi, ma)
    };
}
