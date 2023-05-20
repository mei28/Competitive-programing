use proconio::{fastout, input};
use std::mem::swap;

#[derive(Clone)]
pub struct UnionFind {
    parent: Vec<usize>,
    rank: Vec<usize>,
    size: Vec<usize>,
    group_next: Vec<usize>,
}

impl UnionFind {
    pub fn new(n: usize) -> Self {
        UnionFind {
            parent: (0..n).collect::<Vec<_>>(),
            rank: vec![0; n],
            size: vec![1; n],
            group_next: (0..n).collect::<Vec<_>>(),
        }
    }

    pub fn is_root(&self, x: usize) -> bool {
        return self.parent[x] == x;
    }

    pub fn find(&mut self, x: usize) -> usize {
        if self.is_root(x) {
            return x;
        } else {
            let root = self.find(self.parent[x]);
            self.parent[x] = root;
            return root;
        }
    }

    pub fn union(&mut self, x: usize, y: usize) {
        let (mut root_x, mut root_y) = (self.find(x), self.find(y));
        if root_x == root_y {
            return;
        }

        if self.size[x] < self.size[y] {
            swap(&mut root_x, &mut root_y);
        }

        self.parent[root_y] = root_x;
        self.size[root_x] += self.size[root_y];
    }

    pub fn same(&mut self, x: usize, y: usize) -> bool {
        return self.find(x) == self.find(y);
    }

    pub fn get_size(&mut self, x: usize) -> usize {
        let root = self.find(x);
        return self.size[root];
    }
}

#[fastout]
fn main() {
    input! {
        n: usize,
        m:usize,
        uv: [(usize,usize);m ]
    }

    let mut uf = UnionFind::new(n);
    for &(u, v) in uv.iter() {
        uf.union(u - 1, v - 1);
    }

    let mut cnt = vec![0; n];
    for &(u, _v) in uv.iter() {
        cnt[uf.find(u - 1)] += 1;
    }

    let mut flg = true;
    for i in 0..n {
        if uf.is_root(i) {
            flg &= uf.get_size(i) == cnt[i];
        }
    }

    println!("{}", if flg { "Yes" } else { "No" });
}
