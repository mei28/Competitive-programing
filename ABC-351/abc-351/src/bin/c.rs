use proconio::{fastout, input};
use std::collections::VecDeque;

fn f(deque: &mut VecDeque<usize>) {
    if deque.len() == 1 {
        return;
    }

    let i = deque.pop_back().unwrap();
    let j = deque.pop_back().unwrap();

    if i != j {
        deque.push_back(j);
        deque.push_back(i);
        return;
    }

    if i == j {
        deque.push_back(i + 1);
        f(deque);
    }
}

fn main() {
    input! {n:usize, a:[usize;n]}

    let mut deque = VecDeque::new();

    for i in 0..n {
        deque.push_back(a[i]);
        f(&mut deque);
    }
    println!("{}", deque.len());
}
