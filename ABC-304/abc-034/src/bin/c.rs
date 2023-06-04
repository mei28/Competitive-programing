use proconio::{fastout, input};
use std::mem::swap;

struct UnionFind {
    par: Vec<usize>,
    size: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        UnionFind {
            par: (0..n).collect(),
            size: vec![1; n],
        }
    }

    fn find(&mut self, x: usize) -> usize {
        if self.par[x] == x {
            return x;
        } else {
            let root = self.find(self.par[x]);
            self.par[x] = root;
            return root;
        }
    }

    fn union(&mut self, x: usize, y: usize) {
        let mut x_root = self.find(x);
        let mut y_root = self.find(y);

        if x_root == y_root {
            return;
        }

        if self.size[x_root] > self.size[y_root] {
            swap(&mut x_root, &mut y_root);
        }

        self.par[x_root] = y_root;
        self.size[y_root] += self.size[x_root];
    }

    fn same(&mut self, x: usize, y: usize) -> bool {
        return self.find(x) == self.find(y);
    }
}

fn dist(ax: isize, ay: isize, bx: isize, by: isize) -> usize {
    return ((ax - bx).pow(2) + (ay - by).pow(2)) as usize;
}

#[fastout]
fn main() {
    input! {n:usize,d:usize,xy:[(isize,isize);n]}

    let mut uf = UnionFind::new(n);

    for i in 0..n {
        for j in (i + 1)..n {
            let (ax, ay) = xy[i];
            let (bx, by) = xy[j];
            if dist(ax, ay, bx, by) <= d * d {
                uf.union(i, j);
            }
        }
    }

    for i in 0..n {
        if uf.same(0, i) {
            println!("Yes");
        } else {
            println!("No");
        }
    }
}
