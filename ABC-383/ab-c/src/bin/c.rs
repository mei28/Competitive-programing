use proconio::input;
use std::collections::VecDeque;

fn main() {
    input! {
        h: usize,
        w: usize,
        d: usize,
        grid: [String; h],
    }

    let mut visited = vec![vec![false; w]; h]; 
    let mut queue = VecDeque::new(); 
    let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]; 

    
    for i in 0..h {
        for j in 0..w {
            if grid[i].chars().nth(j).unwrap() == 'H' {
                queue.push_back((i, j, 0)); 
                visited[i][j] = true; 
            }
        }
    }

    let mut humidified_count = 0; 

    while let Some((x, y, dist)) = queue.pop_front() {
        
        if grid[x].chars().nth(y).unwrap() != '#' {
            humidified_count += 1;
        }

        
        for &(dx, dy) in &directions {
            let nx = x as isize + dx;
            let ny = y as isize + dy;

            if nx < 0 || nx >= h as isize || ny < 0 || ny >= w as isize {
                continue; 
            }

            let nx = nx as usize;
            let ny = ny as usize;

            
            if !visited[nx][ny] && grid[nx].chars().nth(ny).unwrap() != '#' && dist + 1 <= d {
                visited[nx][ny] = true; 
                queue.push_back((nx, ny, dist + 1)); 
            }
        }
    }

    println!("{}", humidified_count); 
}

