use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,k:usize,mut ps:[usize;n]}

    ps.sort_by(|a, b| b.cmp(&a));
    println!("{:?}", ps);

    let mut qs = vec![];

    for i in 0..k {
        qs.push(ps[i]);
    }

    let mut ans: f64 = 0.0;
    for i in 0..k {
        let d = (1 + qs[i]) as f64 / 2 as f64;
        ans += d;
    }
    print!("{}", ans );
}
