use proconio::{fastout, input};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {q:usize}
    let mut que = VecDeque::new();

    for _ in 0..q {
        input! {t:usize}
        if t == 1 {
            input! {x:usize,c:usize}
            que.push_back((x, c));
        } else {
            input! {mut c:usize}
            let mut sum = 0;
            while c > 0 {
                let (num, cnt) = que.pop_front().unwrap();
                if c >= cnt {
                    sum += num * cnt;
                    c -= cnt;
                } else {
                    sum += num * c;
                    que.push_front((num, cnt - c));
                    c = 0;
                }
            }
            println!("{}", sum);
        }
    }
}
