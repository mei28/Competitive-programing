use proconio::{fastout, input, marker::Usize1};

#[fastout]
fn main() {
    input! {n:usize}
    let mut G = vec![vec![]; n];

    for _ in 0..n {
        input! {a:Usize1, b:Usize1}
        G[a].push(b);
        G[b].push(a);
    }
}
