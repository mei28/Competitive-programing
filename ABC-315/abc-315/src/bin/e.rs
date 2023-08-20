use itertools::Itertools;
use proconio::{fastout, input, marker::Usize1};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {n:usize}
    let mut graph = vec![];

    for _ in 0..n {
        input! {c:usize,p:[Usize1;c]}
        graph.push(p);
    }

    let mut visited = vec![false; n];
    let mut ans = vec![];
    dfs(&graph, &mut visited, &mut ans, 0);
    println!("{}", ans.iter().take(ans.len() - 1).map(|v| v + 1).join(" "));
}

fn dfs(graph: &Vec<Vec<usize>>, visited: &mut Vec<bool>, ans: &mut Vec<usize>, v: usize) {
    visited[v] = true;
    for u in &graph[v] {
        if visited[*u] {
            continue;
        }
        dfs(graph, visited, ans, *u);
    }
    ans.push(v);
}
