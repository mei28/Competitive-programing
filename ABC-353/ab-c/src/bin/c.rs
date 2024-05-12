use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, mut a:[usize;n]}
    a.sort();

    let mut r = n;
    let mut cnt = 0;
    let mut res = 0;

    for i in 0..n {
        r = r.max(i + 1);

        while r - 1 > i && a[r - 1] + a[i] >= 100000000 {
            r -= 1;
        }
        cnt += n - r;
    }

    for i in 0..n {
        res += a[i] * (n - 1);
    }
    res -= cnt * 100000000;
    println!("{}", res);
}
