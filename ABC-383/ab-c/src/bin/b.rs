use proconio::input;

fn main() {
    input! {
        h: usize,
        w: usize,
        d: usize,
        grid: [String; h], 
    }

    
    let mut floor_positions = vec![];
    for i in 0..h {
        for j in 0..w {
            if grid[i].chars().nth(j).unwrap() == '.' {
                floor_positions.push((i, j));
            }
        }
    }

    let mut max_humidified = 0;

    
    for (k1, &(x1, y1)) in floor_positions.iter().enumerate() {
        for (k2, &(x2, y2)) in floor_positions.iter().enumerate() {
            if k1 >= k2 {
                continue; 
            }

            
            let mut humidified = vec![vec![false; w]; h];
            for i in 0..h {
                for j in 0..w {
                    let dist1 = (x1 as isize - i as isize).abs() + (y1 as isize - j as isize).abs();
                    let dist2 = (x2 as isize - i as isize).abs() + (y2 as isize - j as isize).abs();
                    if dist1 as usize <= d || dist2 as usize <= d {
                        humidified[i][j] = true;
                    }
                }
            }

            
            let count = floor_positions
                .iter()
                .filter(|&&(i, j)| humidified[i][j])
                .count();
            max_humidified = max_humidified.max(count);
        }
    }

    println!("{}", max_humidified);
}

