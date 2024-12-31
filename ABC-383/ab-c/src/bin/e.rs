use std::collections::BinaryHeap;
use std::cmp::Reverse;

struct Edge {
    u: usize,
    v: usize,
    w: u64,
}

fn main() {
    // 入力処理
    let (n, m, k): (usize, usize, usize);
    let mut edges: Vec<Edge> = Vec::new();
    let mut queries: Vec<(usize, usize)> = Vec::new();

    // 入力を受け取る (省略)

    // クラスカル法でMSTを構築
    let mut uf = UnionFind::new(n + 1);
    edges.sort_by_key(|e| e.w); // 重みでソート

    let mut mst = vec![vec![]; n + 1];
    for edge in edges {
        if uf.unite(edge.u, edge.v) {
            mst[edge.u].push((edge.v, edge.w));
            mst[edge.v].push((edge.u, edge.w));
        }
    }

    // ダブリングを用いたLCAの前処理
    let lca = LCA::new(&mst, n);

    // クエリを処理
    let mut max_weights = vec![];
    for &(a, b) in &queries {
        max_weights.push(lca.max_weight(a, b));
    }

    // クエリ結果の最小化
    max_weights.sort();
    let result: u64 = max_weights.into_iter().sum();
    println!("{}", result);
}

// Union-Find構造
struct UnionFind {
    parent: Vec<usize>,
    size: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self {
            parent: (0..n).collect(),
            size: vec![1; n],
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            self.parent[x] = self.find(self.parent[x]);
        }
        self.parent[x]
    }

    fn unite(&mut self, x: usize, y: usize) -> bool {
        let root_x = self.find(x);
        let root_y = self.find(y);

        if root_x != root_y {
            if self.size[root_x] < self.size[root_y] {
                self.parent[root_x] = root_y;
                self.size[root_y] += self.size[root_x];
            } else {
                self.parent[root_y] = root_x;
                self.size[root_x] += self.size[root_y];
            }
            true
        } else {
            false
        }
    }
}

// LCA構造
struct LCA {
    depth: Vec<usize>,
    parent: Vec<Vec<usize>>,
    max_weight: Vec<Vec<u64>>,
}

impl LCA {
    fn new(graph: &Vec<Vec<(usize, u64)>>, n: usize) -> Self {
        let log_n = ((n as f64).log2() as usize) + 1;
        let mut parent = vec![vec![0; log_n]; n + 1];
        let mut max_weight = vec![vec![0; log_n]; n + 1];
        let mut depth = vec![0; n + 1];

        // DFSで親と深さを計算
        fn dfs(
            node: usize,
            parent_node: usize,
            graph: &Vec<Vec<(usize, u64)>>,
            depth: &mut Vec<usize>,
            parent: &mut Vec<Vec<usize>>,
            max_weight: &mut Vec<Vec<u64>>,
        ) {
            for &(next, weight) in &graph[node] {
                if next != parent_node {
                    depth[next] = depth[node] + 1;
                    parent[next][0] = node;
                    max_weight[next][0] = weight;
                    dfs(next, node, graph, depth, parent, max_weight);
                }
            }
        }

        dfs(1, 0, graph, &mut depth, &mut parent, &mut max_weight);

        // ダブリングの前処理
        for j in 1..log_n {
            for i in 1..=n {
                parent[i][j] = parent[parent[i][j - 1]][j - 1];
                max_weight[i][j] = max_weight[i][j - 1].max(max_weight[parent[i][j - 1]][j - 1]);
            }
        }

        Self {
            depth,
            parent,
            max_weight,
        }
    }

    fn max_weight(&self, mut u: usize, mut v: usize) -> u64 {
        let mut max_w = 0;
        if self.depth[u] < self.depth[v] {
            std::mem::swap(&mut u, &mut v);
        }

        let diff = self.depth[u] - self.depth[v];
        let log_n = self.parent[0].len();

        for i in 0..log_n {
            if (diff >> i) & 1 > 0 {
                max_w = max_w.max(self.max_weight[u][i]);
                u = self.parent[u][i];
            }
        }

        if u == v {
            return max_w;
        }

        for i in (0..log_n).rev() {
            if self.parent[u][i] != self.parent[v][i] {
                max_w = max_w.max(self.max_weight[u][i]).max(self.max_weight[v][i]);
                u = self.parent[u][i];
                v = self.parent[v][i];
            }
        }

        max_w.max(self.max_weight[u][0]).max(self.max_weight[v][0])
    }
}
