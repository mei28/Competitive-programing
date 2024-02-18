use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, mut aa:[usize;n], st:[(usize,usize);n-1]}

    for i in 0..n - 1 {
        aa[i + 1] += aa[i] / st[i].0 * st[i].1;
    }

    println!("{}", aa[n - 1]);
}
