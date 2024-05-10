use proconio::{input, marker::Chars};
use std::collections::HashMap;
use std::collections::VecDeque;

fn main() {
    input! {h:usize,w:usize,grid:[Chars;h]}

    let map = HashMap::from([('U', (-1, 0)), ('D', (1, 0)), ('L', (0, -1)), ('R', (0, 1))]);
    let mut que: VecDeque<(usize, usize)> = VecDeque::new();

    let (mut ni, mut nj) = (0, 0);

    let mut visited = vec![vec![false; w]; h];
    visited[ni][nj] = true;

    que.push_back((ni, nj));

    while let Some((i, j)) = que.pop_front() {
        let d = map.get(&grid[i][j]).unwrap();
        let (di, dj) = (i as isize + d.0, j as isize + d.1);

        if di < 0 || di >= h as isize || dj < 0 || dj >= w as isize {
            println!("{} {}", i + 1, j + 1);
            return;
        }
        if visited[di as usize][dj as usize] {
            println!("{}", -1);
            return;
        }
        visited[di as usize][dj as usize] = true;
        que.push_back((di as usize, dj as usize));
    }
}
