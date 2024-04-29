use proconio::{fastout, input};
use std::cmp::Reverse;
use std::collections::BinaryHeap;

const INF: usize = std::usize::MAX;

struct Dijkstra {
    distance: Vec<usize>,
    parent: Vec<usize>,
}

impl Dijkstra {
    // n:usize 頂点の数
    // edge: Vec<Vec<(usize,usize)>> edge[i] = [(2,3), (3,1), (頂点への道,重み)]
    // init:usize どの頂点を起点に考えるか
    pub fn new(n: usize, edge: Vec<Vec<(usize, usize)>>, init: usize) -> Self {
        let mut distance = vec![INF; n];
        let mut parent = vec![INF; n];
        let mut heap = BinaryHeap::new();
        for i in 0..n {
            if i == init {
                // 始点は0
                // BinaryHeapはpopで最大値を取得するので、Reverse()で最小値を取得できるようにする
                heap.push((Reverse(0), i));
            }
            heap.push((Reverse(INF), i));
        }
        while let Some((Reverse(d), target)) = heap.pop() {
            if distance[target] < d {
                // 既にもっと短い経路が見つかってるので無視
                continue;
            }
            distance[target] = d;
            for &(next, cost) in &edge[target] {
                if distance[next] > d + cost {
                    // 短い経路の候補となるので処理を行う
                    distance[next] = d + cost;
                    heap.push((Reverse(distance[next]), next));
                    // ひとつ前の頂点を保存しておく
                    parent[next] = target;
                }
            }
        }
        Self { distance, parent }
    }

    pub fn distance(&self, target: usize) -> usize {
        self.distance[target]
    }

    pub fn get_path(&self, target: usize) -> Vec<usize> {
        let mut current = target;
        let mut res = vec![current];
        while self.parent[current] != INF as usize {
            let next = self.parent[current];
            res.push(next);
            current = next;
        }
        res.reverse();
        res
    }
}
#[fastout]
fn main() {
    input! {n:usize, abx: [(usize,usize,usize);n-1]}

    let mut edges: Vec<Vec<(usize, usize)>> = vec![vec![]; n];

    for (i, (a, b, x)) in abx.iter().enumerate() {
        edges[i].push((i + 1, *a));
        edges[i].push((*x - 1, *b));
    }

    let dijkstra = Dijkstra::new(n, edges, 0);
    println!("{}", dijkstra.distance(n - 1));
}
