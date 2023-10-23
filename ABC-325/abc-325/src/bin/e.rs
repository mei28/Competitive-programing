use proconio::input;
use std::cmp::Reverse;
use std::collections::BinaryHeap;

const INF: i64 = 1e18 as i64;

fn main() {
    input! {
        n: usize,
        a: i64,
        b: i64,
        c: i64,
        d: [[i64; n]; n]
    }

    let mut graph = vec![vec![]; 2 * n];

    for i in 0..n {
        for j in 0..n {
            if i == j {
                continue;
            }
            let cost_car = d[i][j] * a;
            let cost_train = d[i][j] * b + c;

            graph[i].push((j + n, cost_train));
            graph[i + n].push((j + n, cost_train));
            graph[i].push((j, cost_car));
        }
    }

    let mut dist = vec![INF; 2 * n];
    let mut heap = BinaryHeap::new();
    dist[0] = 0;
    heap.push(Reverse((0, 0))); // (distance, vertex)

    while let Some(Reverse((dist_u, u))) = heap.pop() {
        if dist[u] < dist_u {
            continue;
        }

        for &(v, weight) in &graph[u] {
            if dist_u + weight < dist[v] {
                dist[v] = dist_u + weight;
                heap.push(Reverse((dist[v], v)));
            }
        }
    }

    println!("{}", dist[n - 1].min(dist[2 * n - 1]));
}

