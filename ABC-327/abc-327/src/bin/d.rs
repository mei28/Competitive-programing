use proconio::{fastout, input, marker::Usize1};
static mut bipartite: bool = true;

#[fastout]
fn main() {
    input! {n:usize, m:usize, A:[Usize1;m], B:[Usize1;m]}
    let mut visited = vec![-1; n + 1];
    let mut g = vec![vec![]; n + 1];

    for i in 0..m {
        g[A[i]].push(B[i]);
        g[B[i]].push(A[i]);
    }

    for i in 0..n {
        if visited[i] == -1 {
            dfs(i, 0, &mut visited, &g);
        }
    }

    if unsafe { bipartite } {
        println!("Yes");
    } else {
        println!("No");
    }
}

fn dfs(c: usize, x: isize, visited: &mut Vec<isize>, g: &Vec<Vec<usize>>) {
    visited[c] = x;

    for d in g[c].iter() {
        if visited[*d] == -1 {
            dfs(*d, 1 - x, visited, g);
        } else if visited[*d] == visited[c] {
            unsafe { bipartite = false };
        }
    }
}
