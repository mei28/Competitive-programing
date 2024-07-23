use proconio::input;
use std::{cmp::Ordering, collections::BinaryHeap};

const INF: u64 = std::u64::MAX;

#[derive(Clone, PartialEq, Eq)]
pub struct State {
    pub id: usize,
    pub priority: u64,
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        self.priority.cmp(&other.priority).reverse()
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

#[derive(Clone, PartialEq, Eq)]
pub struct Edge {
    pub src: usize,
    pub dst: usize,
    pub weight: u64,
}

#[derive(Clone)]
pub struct Graph {
    pub edges: Vec<Vec<Edge>>,
}

impl Graph {
    pub fn new(n: usize) -> Self {
        Graph {
            edges: vec![vec![]; n],
        }
    }

    pub fn len(&self) -> usize {
        self.edges.len()
    }

    pub fn add_edge(&mut self, src: usize, dst: usize, weight: u64) {
        self.edges[src].push(Edge { src, dst, weight });
    }
}

fn dijkstra(n: usize, start: usize, graph: &Graph, node_weights: &[u64]) -> Vec<u64> {
    let mut dist = vec![INF; n];
    let mut heap = BinaryHeap::new();

    dist[start] = 0;
    heap.push(State {
        id: start,
        priority: 0,
    });

    while let Some(State { id, priority }) = heap.pop() {
        if priority > dist[id] {
            continue;
        }

        for edge in &graph.edges[id] {
            let next_priority = dist[id]
                .checked_add(edge.weight)
                .and_then(|w| w.checked_add(node_weights[edge.dst]))
                .unwrap_or(INF);

            if next_priority < dist[edge.dst] {
                dist[edge.dst] = next_priority;
                heap.push(State {
                    id: edge.dst,
                    priority: next_priority,
                });
            }
        }
    }

    dist
}

fn main() {
    input! {
        n: usize,
        m: usize,
        aa: [u64; n],
        uvb: [(usize, usize, u64); m],
    }

    let mut graph = Graph::new(n);

    for &(u, v, b) in uvb.iter() {
        graph.add_edge(u - 1, v - 1, b);
        graph.add_edge(v - 1, u - 1, b);
    }

    let distances = dijkstra(n, 0, &graph, &aa);

    for (i, &dist) in distances.iter().enumerate() {
        if i == 0 {
            continue;
        }
        if dist == INF {
            println!("INF");
        } else {
            println!("{}", dist + aa[0]);
        }
    }
}
