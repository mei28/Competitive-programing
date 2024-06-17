use proconio::input;

fn main() {
    input! {
        n: usize,
    }

    let carpet = generate_carpet(n);

    for row in carpet {
        println!("{}", row);
    }
}

fn generate_carpet(n: usize) -> Vec<String> {
    if n == 0 {
        return vec![String::from("#")];
    }
    
    let size = 3_usize.pow(n as u32);
    let sub_size = size / 3;
    let smaller_carpet = generate_carpet(n - 1);
    
    let mut carpet = vec![String::with_capacity(size); size];
    
    for i in 0..size {
        let mut row = String::with_capacity(size);
        for j in 0..size {
            if i / sub_size == 1 && j / sub_size == 1 {
                row.push('.');
            } else {
                row.push(smaller_carpet[i % sub_size].chars().nth(j % sub_size).unwrap());
            }
        }
        carpet[i] = row;
    }
    carpet
}

