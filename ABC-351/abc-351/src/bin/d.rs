use proconio::{fastout, input, marker::Chars};
use std::collections::VecDeque;

fn bfs(start_i: usize, start_j: usize, h: usize, w: usize, ss: &Vec<Vec<char>>) -> usize {
    let mut visited = vec![vec![false; w]; h];
    let mut queue = VecDeque::new();
    queue.push_back((start_i, start_j));
    visited[start_i][start_j] = true;
    let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)];
    let mut count = 1;

    while let Some((i, j)) = queue.pop_front() {
        if !any_magnet_adjacent(i, j, h, w, ss) {
            // Check if it's not adjacent to a magnet
            for (di, dj) in directions.iter() {
                let new_i = i as i32 + di;
                let new_j = j as i32 + dj;
                if new_i >= 0 && new_i < h as i32 && new_j >= 0 && new_j < w as i32 {
                    let new_i = new_i as usize;
                    let new_j = new_j as usize;
                    if !visited[new_i][new_j] && ss[new_i][new_j] == '.' {
                        visited[new_i][new_j] = true;
                        queue.push_back((new_i, new_j));
                        count += 1;
                    }
                }
            }
        }
    }
    count
}

fn any_magnet_adjacent(i: usize, j: usize, h: usize, w: usize, ss: &Vec<Vec<char>>) -> bool {
    for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
        let ni = i as i32 + di;
        let nj = j as i32 + dj;
        if ni >= 0 && ni < h as i32 && nj >= 0 && nj < w as i32 {
            if ss[ni as usize][nj as usize] == '#' {
                return true;
            }
        }
    }
    false
}

#[fastout]
fn main() {
    input! {h: usize, w: usize, ss: [Chars; h]}
    let mut max_freedom = 0;
    for i in 0..h {
        for j in 0..w {
            if ss[i][j] == '.' {
                let freedom = bfs(i, j, h, w, &ss);
                max_freedom = max_freedom.max(freedom);
            }
        }
    }
    println!("{}", max_freedom);
}

