use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, x:[usize;n]}
    let mut y = x.clone();
    y.sort();

    for i in 0..n {
        if x[i] < y[n / 2] {
            println!("{}", y[n / 2]);
        } else {
            println!("{}", y[n / 2 - 1]);
        }
    }
}
