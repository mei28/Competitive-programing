use proconio::{input, marker::Chars};
use std::cmp::{max, min};
use std::collections::VecDeque;

fn check(
    i: usize,
    m: usize,
    used: &mut Vec<bool>,
    s: &Vec<char>,
    t: &Vec<char>,
    q: &mut VecDeque<usize>,
) {
    if used[i] || i + m > s.len() {
        return;
    }
    let mut ok = true;

    for j in 0..m {
        ok &= s[i + j] == '#' || s[i + j] == t[j];
    }
    if ok {
        used[i] = true;
        q.push_back(i);
    }
}

fn main() {
    input! {
        n:usize,
        m:usize,
    mut s:Chars,
        t:Chars,
    }

    let mut used = vec![false; n - m + 1];
    let mut que: VecDeque<usize> = VecDeque::new();

    for i in 0..n - m + 1 {
        check(i, m, &mut used, &s, &t, &mut que);
    }

    while let Some(i) = que.pop_front() {
        for j in 0..m {
            if i + j < s.len() {
                s[i + j] = '#';
            }
        }
        for k in max(i as isize - m as isize + 1, 0) as usize..=min(i + m - 1, n - m) {
            check(k, m, &mut used, &mut s, &t, &mut que);
        }
    }

    let ans = s.iter().all(|&c| c == '#');
    println!("{}", if ans { "Yes" } else { "No" });
}
