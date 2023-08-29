use proconio::{fastout, input, marker::Chars};
use std::collections::VecDeque;

#[derive(Clone, PartialEq, Eq, Debug)]
pub struct Edge<T> {
    pub src: usize,
    pub dst: usize,
    pub weight: T,
}
#[derive(Clone, Debug)]
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
        self.edges[src].push(Edge { src, dst, weight })
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
    input! {h: usize, w: usize, mut a: [Chars; h]}

    let s = || -> (usize, usize) {
        for i in 0..h {
            for j in 0..w {
                if a[i][j] == 'S' {
                    a[i][j] = '.';
                    return (i, j);
                }
            }
        }
        unreachable!()
    }();

    let g = || -> (usize, usize) {
        for i in 0..h {
            for j in 0..w {
                if a[i][j] == 'G' {
                    a[i][j] = '.';
                    return (i, j);
                }
            }
        }
        unreachable!()
    }();
    let mut board = vec![vec![true; w]; h];

    for i in 0..h {
        for j in 0..w {
            match a[i][j] {
                '>' => {
                    let mut j = j;
                    loop {
                        board[i][j] = false;
                        j += 1;
                        if j >= w || a[i][j] != '.' {
                            break;
                        }
                    }
                }
                '^' => {
                    let mut i = i;
                    loop {
                        board[i][j] = false;
                        if i == 0 {
                            break;
                        }
                        i -= 1;
                        if a[i][j] != '.' {
                            break;
                        }
                    }
                }
                '<' => {
                    let mut j = j;
                    loop {
                        board[i][j] = false;
                        if j == 0 {
                            break;
                        }
                        j -= 1;
                        if a[i][j] != '.' {
                            break;
                        }
                    }
                }
                'v' => {
                    let mut i = i;
                    loop {
                        board[i][j] = false;
                        i += 1;
                        if i >= h || a[i][j] != '.' {
                            break;
                        }
                    }
                }
                '#' => {
                    board[i][j] = false;
                }
                _ => {}
            }
        }
    }
    let mut graph = Graph::new(h * w);
    for i in 0..h - 1 {
        for j in 0..w {
            if board[i][j] && board[i + 1][j] {
                graph.add_edge(w * i + j, w * (i + 1) + j, 1);
                graph.add_edge(w * (i + 1) + j, w * i + j, 1);
            }
        }
    }

    for i in 0..h {
        for j in 0..w - 1 {
            if board[i][j] && board[i][j + 1] {
                graph.add_edge(w * i + j, w * i + j + 1, 1);
                graph.add_edge(w * i + j + 1, w * i + j, 1);
            }
        }
    }

    let bfs = graph.bfs(w * s.0 + s.1);
    if let Some(ans) = bfs.get_distance(w * g.0 + g.1) {
        println!("{}", ans);
    } else {
        println!("-1");
    }
}
