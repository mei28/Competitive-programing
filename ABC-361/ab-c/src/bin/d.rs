use itertools::Itertools;
use proconio::{fastout, input, marker::Chars};
use std::collections::{HashMap, VecDeque};

#[fastout]
fn main() {
    input! {
        _n: usize,
        mut s: Chars,
        mut t: Chars,
    }

    s.push('.');
    s.push('.');
    t.push('.');
    t.push('.');

    let mut memo: HashMap<Vec<char>, usize> = HashMap::new();
    memo.insert(s.clone(), 0);

    let mut stack = VecDeque::new();
    stack.push_back(s.clone());

    while let Some(s) = stack.pop_front() {
        let i = (0..).find(|&k| s[k] == '.').unwrap();
        let j = (i + 1..).find(|&k| s[k] == '.').unwrap();
        for k in 0..s.len() - 1 {
            if s[k] != '.' && s[k + 1] != '.' {
                let mut t = s.clone();
                t.swap(k, i);
                t.swap(k + 1, j);
                if !memo.contains_key(&t) {
                    memo.insert(t.clone(), *memo.get(&s.clone()).unwrap() + 1);
                    stack.push_back(t.clone());
                }
            }
        }
    }

    if let Some(ans) = memo.get(&t) {
        println!("{}", ans);
    } else {
        println!("-1");
    }
}

