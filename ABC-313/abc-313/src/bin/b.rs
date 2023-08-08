use proconio::input;
use std::collections::VecDeque;

fn main() {
    input! {
        n: usize,
        m: usize,
        ab: [(usize, usize); m]
    }

    let mut graph = vec![VecDeque::new(); n + 1];
    let mut not_weakest = vec![false; n + 1];

    for &(a, b) in &ab {
        graph[a].push_back(b);
        not_weakest[b] = true;
    }

    let mut strongest = Vec::new();

    for i in 1..=n {
        if !not_weakest[i] {
            strongest.push(i);
        }
    }

    if strongest.len() != 1 {
        println!("-1");
        return;
    }

    let mut visited = vec![false; n + 1];
    let mut stack = Vec::new();
    stack.push(strongest[0]);

    while let Some(node) = stack.pop() {
        if visited[node] {
            continue;
        }
        visited[node] = true;
        for &next_node in &graph[node] {
            stack.push(next_node);
        }
    }

    if visited.iter().skip(1).all(|&x| x) {
        println!("{}", strongest[0]);
    } else {
        println!("-1");
    }
}

