use proconio::{fastout, input, marker::Usize1};
fn dfs(
    graph: &Vec<Vec<usize>>,
    path: &mut Vec<usize>,
    visited: &mut Vec<bool>,
    c: usize,
    ans: &mut usize,
    limit: usize,
) {
    if *ans >= limit {
        return;
    }
    visited[c] = true;
    path.push(c);
    *ans += 1;

    for &d in &graph[c] {
        if visited[d] {
            continue;
        }
        dfs(graph, path, visited, d, ans, limit)
    }
    visited[c] = false;
    path.pop();
}

#[fastout]
fn main() {
    input! {n:usize, m:usize, uv:[(Usize1, Usize1); m]}
    let mut graph = vec![vec![]; n];

    for (u, v) in uv.into_iter() {
        graph[u].push(v);
        graph[v].push(u);
    }

    let mut visited = vec![false; n];
    let mut path = vec![];
    let mut ans = 0;
    let limit = 1000000;

    dfs(&graph, &mut path, &mut visited, 0, &mut ans, limit);
    println!("{}", ans);
}
