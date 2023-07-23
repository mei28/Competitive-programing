use proconio::{fastout, input, marker::*};
use std::collections::VecDeque;

const DX: [isize; 4] = [1, 0, -1, 0];
const DY: [isize; 4] = [0, -1, 0, 1];

#[fastout]
fn main() {
    input! {
        n: usize,m:usize,
        grid: [Chars;n],
    }

    let mut visited = vec![vec![vec![false; 4]; m]; n];
    let x = 1;
    let y = 1;
    for i in 0..4 {
        visited[x][y][i] = true;
    }
    let mut q = VecDeque::new();
    for i in 0..4 {
        q.push_back((x, y, i));
    }

    while let Some(t) = q.pop_front() {
        let nx = (t.0 as isize + DX[t.2]) as usize;
        let ny = (t.1 as isize + DY[t.2]) as usize;

        if nx >= n || ny >= m || grid[nx][ny] == '#' {
            for i in 0..4 {
                if i != t.2 && !visited[t.0][t.1][i] {
                    visited[t.0][t.1][i] = true;
                    q.push_back((t.0, t.1, i));
                }
            }
        } else if !visited[nx][ny][t.2] {
            visited[nx][ny][t.2] = true;
            q.push_back((nx, ny, t.2));
        }
    }

    let mut reachble_ice = 0;
    for i in 0..n {
        for j in 0..m {
            reachble_ice += if visited[i][j].iter().any(|&x| x) {
                1
            } else {
                0
            };
        }
    }
    println!("{}", reachble_ice);
}

