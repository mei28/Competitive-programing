use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {n:usize,k:usize}

    let mut edge = vec![HashSet::new(); n];

    for _ in 0..n - 1 {
        input! {a:usize,b:usize}
        edge[a - 1].insert(b - 1);
        edge[b - 1].insert(a - 1);
    }

    let mut V: HashSet<usize> = {
        input! {v:[usize;k]}
        HashSet::from_iter(v.iter().map(|&x| x - 1))
    };

    let deg = (0..n).map(|i| edge[i].len()).collect::<Vec<usize>>();
    let mut q = (0..n).filter(|&i| deg[i] == 1).collect::<Vec<usize>>();

    let mut ans = n;
    while let Some(v) = q.pop() {
        if V.contains(&v) {
            continue;
        }
        let vv = *edge[v].iter().next().unwrap();
        edge[vv].remove(&v);
        ans -= 1;
        if edge[vv].len() == 1 {
            q.push(vv);
        }
    }
    println!("{}", ans);
}
