use proconio::{fastout, input, marker::Usize1};

#[derive(Clone)]
struct Edge<T> {
    from: usize,
    to: usize,
    cost: T,
}

#[derive(Clone)]
struct Graph<T> {
    edges: Vec<Vec<Edge<T>>>,
}

impl<T> Graph<T>
where
    T: Clone,
{
    fn new(n: usize) -> Self {
        Graph {
            edges: vec![vec![]; n],
        }
    }

    fn add_edge(&mut self, from: usize, to: usize, cost: T) {
        self.edges[from].push(Edge { from, to, cost });
    }
}
fn rec<T>(graph: &Graph<T>, v: usize, p: Option<usize>, sum: T, dist: &mut Vec<T>)
where
    T: Copy + std::ops::Add<Output = T>,
{
    dist[v] = sum;

    for e in &graph.edges[v] {
        if Some(e.to) == p {
            continue;
        }
        rec(graph, e.to, Some(v), sum + e.cost, dist);
    }
}

#[fastout]
fn main() {
    input! {
        n:usize,
    }
    let mut graph = Graph::new(n);
    for _ in 0..n - 1 {
        input! {
            a:Usize1,
            b:Usize1,
            c:isize,
        }
        graph.add_edge(a, b, c);
        graph.add_edge(b, a, c);
    }
    input! { mut q:usize,k:Usize1 }
    let mut dist = vec![0; n];
    rec(&graph, k, None, 0, &mut dist);

    while q > 0 {
        input! {x:Usize1,y:Usize1}
        println!("{}", dist[x] + dist[y]);
        q -= 1;
    }
}
