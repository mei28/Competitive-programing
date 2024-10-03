use proconio::input;

struct UnionFind {
    par: Vec<usize>,
    size: Vec<usize>,
    weight: Vec<i64>, // weight from each node to its parent
}

impl UnionFind {
    fn new(n: usize) -> Self {
        UnionFind {
            par: (0..n).collect(),
            size: vec![1; n],
            weight: vec![0; n], // initialize all weights to 0
        }
    }

    fn root(&mut self, x: usize) -> usize {
        if self.par[x] == x {
            return x;
        }
        let parent = self.par[x];
        let root = self.root(parent);
        self.weight[x] += self.weight[parent]; // update the weight to the root
        self.par[x] = root;
        root
    }

    fn union(&mut self, mut x: usize, mut y: usize, mut w: i64) -> bool {
        w += self.weight(x);
        w -= self.weight(y);

        x = self.root(x);
        y = self.root(y);

        if x == y {
            return false;
        }

        if self.size[x] < self.size[y] {
            std::mem::swap(&mut x, &mut y);
            w = -w;
        }

        self.par[y] = x;
        self.size[x] += self.size[y];
        self.weight[y] = w;
        true
    }

    fn same(&mut self, x: usize, y: usize) -> bool {
        self.root(x) == self.root(y)
    }

    fn diff(&mut self, x: usize, y: usize) -> i64 {
        self.weight(y) - self.weight(x)
    }

    fn weight(&mut self, x: usize) -> i64 {
        self.root(x); // ensure path compression is done
        self.weight[x]
    }

    fn size(&mut self, x: usize) -> usize {
        let root = self.root(x);
        self.size[root]
    }
}
fn main() {
    input! {n:usize,m:usize}
    let mut uf = UnionFind::new(n);

    for _ in 0..m {
        input! {mut u:usize,mut v:usize,w:i64}
        u -= 1;
        v -= 1;
        uf.union(u, v, w);
    }

    for i in 0..n {
        println!("{}", uf.weight(i));
    }
}
