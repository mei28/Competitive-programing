use proconio::input;

fn dfs(graph: &Vec<Vec<(usize, i64)>>, v: usize) -> Vec<i64> {
    let n = graph.len();
    let mut dist = vec![-1; n];
    dist[v] = 0;

    let mut stack = vec![v];

    while let Some(u) = stack.pop() {
        for &(i, weight) in &graph[u] {
            if dist[i] == -1 {
                stack.push(i);
                dist[i] = dist[u] + weight;
            }
        }
    }
    dist
}

fn main() {
    input! {
        n: usize,
        abc: [(usize, usize, i64); n - 1],
    }

    let mut graph = vec![vec![]; n];
    let mut cs = 0;

    for (a, b, c) in abc {
        graph[a - 1].push((b - 1, c));
        graph[b - 1].push((a - 1, c));
        cs += c;
    }

    let dist = dfs(&graph, 0);
    let mut mx = -1;
    let mut mv = 0;

    for v in 0..n {
        if mx < dist[v] {
            mx = dist[v];
            mv = v;
        }
    }

    let dist = dfs(&graph, mv);
    let mut mx = -1;
    for v in 0..n {
        if mx < dist[v] {
            mx = dist[v];
        }
    }
    println!("{}", 2 * cs - mx);
}

