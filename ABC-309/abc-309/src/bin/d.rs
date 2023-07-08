use proconio::{fastout, input, marker::Usize1};
use std::collections::VecDeque;

#[derive(Clone, PartialEq, Eq, Debug)]
pub struct Edge<T> {
    pub src: usize,
    pub dst: usize,
    pub weight: T,
}

pub struct Graph<T> {
    pub edges: Vec<Vec<Edge<T>>>,
}

impl<T> Graph<T>
where
    T: Clone,
{
    pub fn new(n: usize) -> Self {
        Graph {
            edges: vec![vec![]; n],
        }
    }

    pub fn len(&self) -> usize {
        self.edges.len()
    }

    pub fn add_edge(&mut self, src: usize, dst: usize, weight: T) {
        self.edges[src].push(Edge { src, dst, weight });
    }
}

pub struct Bfs {
    start: usize,
    dist: Vec<Option<usize>>,
    prev: Vec<Option<usize>>,
}
impl<T> Graph<T>
where
    T: Clone,
{
    pub fn bfs(&self, start: usize) -> Bfs {
        let mut dist = vec![None; self.len()];
        dist[start] = Some(0);
        let mut que = VecDeque::new();
        que.push_back(start);
        let mut prev = vec![None; self.len()];

        while let Some(node) = que.pop_front() {
            for e in &self.edges[node] {
                if dist[e.dst].is_none() {
                    prev[e.dst] = Some(e.src);
                    dist[e.dst] = Some(dist[e.src].unwrap() + 1);
                    que.push_back(e.dst);
                }
            }
        }

        Bfs { start, dist, prev }
    }
}
impl Bfs {
    pub fn get_start(&self) -> usize {
        self.start
    }

    pub fn get_distance(&self, dst: usize) -> Option<usize> {
        self.dist[dst]
    }

    pub fn get_path(&self, dst: usize) -> Option<Vec<usize>> {
        self.dist[dst]?;

        let mut prev = self.prev[dst];
        let mut res = vec![dst];
        while let Some(p) = prev {
            res.push(p);
            prev = self.prev[p];
        }
        res.reverse();

        Some(res)
    }
}

#[fastout]
fn main() {
    input! {
        n1: usize, n2: usize, m: usize,
        ab: [(Usize1, Usize1); m],
    }

    let mut g = Graph::new(n1 + n2);
    for &(a, b) in ab.iter() {
        g.add_edge(a, b, 1);
        g.add_edge(b, a, 1);
    }

    let bfs1 = g.bfs(0);
    let bfs2 = g.bfs(n1 + n2 - 1);
    let d1 = (0..n1)
        .map(|v| bfs1.get_distance(v).unwrap())
        .max()
        .unwrap();
    let d2 = (n1..n1 + n2)
        .map(|v| bfs2.get_distance(v).unwrap())
        .max()
        .unwrap();
    println!("{}", d1 + d2 + 1);
}
