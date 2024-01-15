use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, mut a:[usize;n]}

    let mut l = vec![];
    let mut r = vec![];

    let mut cnt = 0;

    for i in 0..n {
        if cnt <= a[i] {
            cnt += 1;
        } else {
            cnt = a[i];
        }
        l.push(cnt);
    }
    a.reverse();
    for i in 0..n {
        if cnt < a[i] {
            cnt += 1;
        } else {
            cnt = a[i];
        }
        r.push(cnt);
    }
    r.reverse();

    println!(
        "{}",
        l.iter().zip(r.iter()).map(|x| x.0.min(x.1)).max().unwrap()
    );
}
