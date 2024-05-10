use proconio::input;
use std::collections::VecDeque;

fn main() {
    input! {
        n:usize,m:usize,
        ab:[(usize,usize);m],
        q:usize,
        xk:[(usize,usize);q],
    }

    let mut edges: Vec<Vec<usize>> = vec![vec![]; n];

    for (a, b) in ab {
        edges[a - 1].push(b - 1);
        edges[b - 1].push(a - 1);
    }

    let mut dis = vec![-1; n];

    for (x, k) in xk {}
}
