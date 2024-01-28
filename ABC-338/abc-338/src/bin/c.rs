use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n:usize,
        q:[usize;n],
        a:[usize;n],
        b:[usize;n]
    }

    let mut ans = 0;
    let inf = std::usize::MAX;
    let max_q = q.iter().max().unwrap();

    for x in 0..=*max_q {
        let mut y = inf;
        for i in 0..n {
            if q[i] < a[i] * x {
                y = std::usize::MIN; // -inf に相当する最小値を使用
            } else if b[i] > 0 {
                y = std::cmp::min(y, (q[i] - a[i] * x) / b[i]);
            }
        }
        ans = std::cmp::max(ans, x + y);
    }
    println!("{}", ans);
}
