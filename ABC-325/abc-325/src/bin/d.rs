use proconio::input;
use std::collections::BinaryHeap;
use std::cmp::Reverse;

fn main() {
    input! {
        n: usize,
        td: [(i64, i64); n]
    }

    let mut v: Vec<(i64, i64)> = td.iter().map(|&(a, b)| (a, a + b)).collect();
    v.sort_by(|a, b| a.0.cmp(&b.0));

    let mut pq = BinaryHeap::new();
    let mut it = 0;
    let mut ans = 0;
    let mut i = 0;

    loop {
        if pq.is_empty() {
            if it == n {
                break;
            }
            i = v[it].0;
        }
        while it < n && v[it].0 == i {
            pq.push(Reverse(v[it].1));
            it += 1;
        }
        while !pq.is_empty() && pq.peek().unwrap().0 < i {
            pq.pop();
        }
        if !pq.is_empty() {
            pq.pop();
            ans += 1;
        }
        i += 1; // Increment the time
    }

    println!("{}", ans);
}

