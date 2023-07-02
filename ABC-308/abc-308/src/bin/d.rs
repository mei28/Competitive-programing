use proconio::{fastout, input, marker::*};
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
        h: usize,
        w: usize,
        ss: [Chars; h],
    }

    let dx = [0, 0, 1, -1];
    let dy = [1, -1, 0, 0];

    let snuke = ['s', 'n', 'u', 'k', 'e'];

    let mut visited = vec![vec![vec![false; 5]; w]; h];
    let mut que = VecDeque::new();
    que.push_back((0, 0, 0));

    visited[0][0][0] = true;

    while let Some((x, y, t)) = que.pop_front() {
        for i in 0..4 {
            let nx = x as isize + dx[i];
            let ny = y as isize + dy[i];
            let nt = (t + 1) % 5;

            if nx < 0 || nx >= h as isize || ny < 0 || ny >= w as isize {
                continue;
            }

            if visited[nx as usize][ny as usize][nt] {
                continue;
            }

            if ss[nx as usize][ny as usize] == snuke[nt] {
                que.push_back((nx, ny, nt));
                visited[nx as usize][ny as usize][nt] = true;
            }
        }
    }

    if visited[h - 1][w - 1].iter().any(|x| *x) {
        println!("{}", "Yes");
    } else {
        println!("{}", "No");
    }
}
