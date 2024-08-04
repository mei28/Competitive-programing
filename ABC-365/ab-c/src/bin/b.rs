use proconio::{fastout, input};

fn main() {
    input! {n:usize, aa:[usize;n]}
    let mut bb = aa.clone();
    bb.sort();
    let b = bb[n - 2];
    let ans = aa.iter().position(|&a| a == b).unwrap();
    print!("{}", ans + 1);
}
