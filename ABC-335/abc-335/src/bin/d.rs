use proconio::input;

fn main() {
    input! { n: usize, }

    let mut grid = vec![vec!["".to_string(); n]; n];
    let mut x = n / 2;
    let mut y = n / 2;
    grid[x][y] = "T".to_string();

    let mut dx = 0;
    let mut dy = -1;
    let mut step = 1;
    let mut num = 1;

    while num < n * n {
        for _ in 0..2 {
            for _ in 0..step {
                if num >= n * n {
                    break;
                }
                x = (x as i32 + dx) as usize;
                y = (y as i32 + dy) as usize;
                grid[x][y] = num.to_string();
                num += 1;
            }
            let temp = dx;
            dx = -dy;
            dy = temp;
        }
        step += 1;
    }

    for row in grid {
        for val in row {
            print!("{:3} ", val);
        }
        println!();
    }
}
