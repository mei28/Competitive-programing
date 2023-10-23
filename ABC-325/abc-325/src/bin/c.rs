use proconio::{fastout, input, marker::Chars};

const DX: [isize; 8] = [-1, 0, 1, -1, 1, -1, 0, 1];
const DY: [isize; 8] = [-1, -1, -1, 0, 0, 1, 1, 1];

fn dfs(
    i: usize,
    j: usize,
    h: usize,
    w: usize,
    grid: &Vec<Vec<char>>,
    visited: &mut Vec<Vec<bool>>,
) {
    visited[i][j] = true;

    for d in 0..8 {
        let ni = i as isize + DX[d];
        let nj = j as isize + DY[d];

        if ni < 0 || ni >= h as isize || nj < 0 || nj >= w as isize {
            continue;
        }
        let ni = ni as usize;
        let nj = nj as usize;

        if grid[ni][nj] == '#' && !visited[ni][nj] {
            dfs(ni, nj, h, w, grid, visited);
        }
    }
}

#[fastout]
fn main() {
    input! {h:usize,w:usize,S:[Chars;h]}
    let grid = S.iter().map(|s| s.clone()).collect::<Vec<_>>();
    let mut visited = vec![vec![false; w]; h];

    let mut count = 0;
    for i in 0..h {
        for j in 0..w {
            if grid[i][j] == '#' && !visited[i][j] {
                dfs(i, j, h, w, &grid, &mut visited);
                count += 1;
            }
        }
    }

    println!("{}", count);
}
