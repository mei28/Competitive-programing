use proconio::{fastout, input, marker::Usize1};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {n:usize,m:usize,abxy:[(Usize1,Usize1,isize,isize);m]}

    let mut xys = vec![vec![]; n];

    for &(a, b, x, y) in abxy.iter() {
        xys[a].push((b, x, y));
        xys[b].push((a, -x, -y));
    }

    let mut ans = vec![None; n];
    ans[0] = Some((0, 0));

    let mut q = VecDeque::new();
    q.push_back(0);

    while let Some(v) = q.pop_front() {
        let tmp = ans.get(v).unwrap().unwrap();

        for &e in xys.get(v).unwrap() {
            if ans[e.0].is_some() {
                continue;
            }
            ans[e.0] = Some((tmp.0 + e.1, tmp.1 + e.2));
            q.push_back(e.0);
        }
    }

    for ans in ans {
        if ans.is_none() {
            println!("undecidable");
        } else {
            println!("{} {}", ans.unwrap().0, ans.unwrap().1);
        }
    }
}
