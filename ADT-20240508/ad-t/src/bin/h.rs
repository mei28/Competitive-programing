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

    let mut dis: Vec<isize> = vec![-1; n];

    for (mut x, k) in xk {
        x -= 1;
        let mut que = VecDeque::new();
        dis[x] = 0;
        let mut vs: Vec<usize> = vec![];

        while let Some(u) = que.pop_front() {
            vs.push(u);
            if dis[u] == k as isize {
                continue;
            }

            for j in 0..edges[u].len() {
                let v = edges[u][j];
                if dis[v] != -1 {
                    continue;
                }
                dis[v] = dis[u] + 1;
                que.push_back(v);
            }
        }
        let mut ans = 0;
        for j in 0..vs.len() {
            ans += vs[j] + 1;
            dis[vs[j]] = -1;
        }
        println!("{}", ans);
    }
}
