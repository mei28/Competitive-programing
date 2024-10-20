use proconio::input;
use std::mem::swap;

fn num_move(n: usize, mut from: usize, mut to: usize, ng: usize) -> usize {
    if from > to {
        swap(&mut from, &mut to);
    }
    if from < ng && ng < to {
        n + from - to
    } else {
        to - from
    }
}

fn main() {
    input! {n:usize,q:usize}
    let mut l = 1;
    let mut r = 2;

    let mut ans = 0;
    for _ in 0..q {
        input! {h:char,t:usize}
        if h == 'L' {
            ans += num_move(n, l, t, r);
            l = t;
        } else {
            ans += num_move(n, r, t, l);
            r = t;
        }
    }
    println!("{}", ans);
}
