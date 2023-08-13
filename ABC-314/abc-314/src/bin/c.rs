use itertools::Itertools;
use proconio::{
    fastout, input,
    marker::{Chars, Usize1},
};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
        n:usize,
        m:usize,
        s:Chars,
        c:[Usize1;n],
    }

    let mut deque = vec![VecDeque::new(); m];

    for i in 0..n {
        deque[c[i]].push_back(s[i]);
    }

    for i in 0..m {
        if deque[i].len() == 0 {
            continue;
        }

        let x = deque[i].pop_back().unwrap();
        deque[i].push_front(x);
    }

    let mut ans = vec![];

    for i in 0..n {
        ans.push(deque[c[i]].pop_front().unwrap());
    }

    println!("{}", ans.into_iter().join(""));
}
