use petgraph::unionfind::UnionFind;
use proconio::{fastout, input, marker::Usize1};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {n:usize,m:usize,uv:[(Usize1,Usize1);m]}
    let mut uf = UnionFind::new(n);

    for (u, v) in uv.into_iter() {
        uf.union(u, v);
    }

    let mut set = HashSet::new();

    for i in 0..n {
        set.insert(uf.find(i));
    }

    println!("{}", set.len());
}
