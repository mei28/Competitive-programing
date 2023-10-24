use proconio::{fastout, input, marker::Usize1};
use std::cmp::max;
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {n:usize}
    let mut g = vec![vec![]; n];

    for i in 0..n - 1 {
        input! {a:Usize1, b:Usize1}
        g[a].push((b, i));
        g[b].push((a, i));
    }

    let mut max_color = 0;

    for i in 0..n {
        max_color = max(max_color, g[i].len())
    }

    let mut res: Vec<isize> = vec![-1; n - 1];
    let mut dist: Vec<isize> = vec![-1; n];

    let mut que: VecDeque<(usize, isize)> = VecDeque::new();

    que.push_back((0, -1));
    dist[0] = 0;

    while let Some(p) = que.pop_front() {
        let v = p.0 as usize;
        let c = p.1;
        let mut color = 1;
        if color == c {
            color += 1;
        }

        for &u in &g[v] {
            if dist[u.0] == -1 {
                dist[u.0] = dist[v] + 1;
                que.push_back((u.0, color));
                res[u.1] = color;
                color += 1;
                if color == c {
                    color += 1;
                }
            }
        }
    }

    println!("{}", max_color);
    for &v in &res {
        println!("{}", v);
    }
}

