use proconio::{fastout, input};
use std::cmp::{max, min};

#[fastout]
fn main() {
    input! {
        x:usize,
        y:usize,
        a:usize,
        b:usize,
        c:usize,
        mut p:[usize;a],
        mut q:[usize;b],
        mut r:[usize;c],
    }

    p.sort_by(|a, b| b.cmp(a));
    q.sort_by(|a, b| b.cmp(a));
    r.sort_by(|a, b| b.cmp(a));

    let mut pq = vec![];
    for i in 0..x {
        pq.push(p[i]);
    }
    for i in 0..y {
        pq.push(q[i]);
    }
    pq.sort_by(|a, b| b.cmp(a));

    let mut sum_pq = vec![0];

    for i in 0..x + y {
        sum_pq.push(sum_pq[i] + pq[i]);
    }

    r.sort_by(|a, b| b.cmp(a));
    let mut sum_r = vec![0];
    for i in 0..c {
        sum_r.push(sum_r[i] + r[i]);
    }

    let mut ans = 0;

    for i in 0..=min(c, x + y) {
        ans = max(ans, sum_pq[x + y - i] + sum_r[i]);
    }
    println!("{}", ans);
}
