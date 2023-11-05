use proconio::{fastout, input};
use std::collections::HashSet;

fn is_valid_sudoku(grid: &Vec<Vec<usize>>) -> bool {
    for i in 0..9 {
        let mut row: HashSet<usize> = HashSet::new();
        let mut col: HashSet<usize> = HashSet::new();
        let mut block: HashSet<usize> = HashSet::new();
        for j in 0..9 {
            if row.contains(&grid[i][j]) {
                return false;
            }
            row.insert(grid[i][j]);

            if col.contains(&grid[j][i]) {
                return false;
            }
            col.insert(grid[j][i]);
            let block_row = 3 * (i / 3);
            let block_col = 3 * (i % 3);
            if block.contains(&grid[block_row + j / 3][block_col + j % 3]) {
                return false;
            }
            block.insert(grid[block_row + j / 3][block_col + j % 3]);
        }
    }
    return true;
}

#[fastout]
fn main() {
    input! {grid: [[usize;9];9]}
    let ans = is_valid_sudoku(&grid);
    if ans {
        println!("Yes")
    } else {
        println!("No")
    }
}
