use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,mut a:[usize;n]}

    let mut sum = 0;
    for i in 0..n {
        sum += a[i];
    }

    a.sort();

    let mut b = vec![sum / n; n];

    for i in 0..(sum % n) {
        b[n - 1 - i] += 1;
    }

    let mut ans = 0;

    for i in 0..n {
        ans += (a[i] as i64 - b[i] as i64).abs();
    }
    println!("{}", ans);
}
