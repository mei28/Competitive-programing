use proconio::input;

fn main() {
    input! {
        n: usize,
        mut grid: [String; n],
    }

    let mut grid: Vec<Vec<char>> = grid.into_iter().map(|row| row.chars().collect()).collect();

    let mut new_grid = grid.clone();

    for i in 0..(n / 2) {
        for x in i..(n - i) {
            for y in i..(n - i) {
                new_grid[y][n - 1 - x] = grid[x][y];
            }
        }
    }

    for row in new_grid {
        println!("{}", row.into_iter().collect::<String>());
    }
}

