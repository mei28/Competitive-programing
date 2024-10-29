use proconio::input;
use std::collections::HashSet;

fn move_knight(x: usize, y: usize, n: usize) -> Vec<(usize, usize)> {
    let mut res = Vec::new();
    let dx = [-2, -2, -1, -1, 1, 1, 2, 2];
    let dy = [-1, 1, -2, 2, -2, 2, -1, 1];
    for i in 0..8 {
        let nx = x as i32 + dx[i];
        let ny = y as i32 + dy[i];
        if nx >= 0 && ny >= 0 && nx < n as i32 && ny < n as i32 {
            res.push((nx as usize, ny as usize));
        }
    }
    res
}

fn main() {
    input! {n:usize,m:usize}

    let mut set = HashSet::new();

    for _ in 0..m {
        input! {a:usize,b:usize}
        set.insert((a - 1, b - 1));
        let movi = move_knight(a - 1, b - 1, n);
        for m in movi {
            set.insert(m);
        }
    }
    println!("{}", n * n - set.len());
}
