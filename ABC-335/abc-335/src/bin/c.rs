use proconio::{fastout, input};
use std::collections::{HashMap, VecDeque};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut q: usize,
    }

    let mut direction: HashMap<String, (i32, i32)> = HashMap::new();
    direction.insert("R".to_string(), (1, 0));
    direction.insert("L".to_string(), (-1, 0));
    direction.insert("U".to_string(), (0, 1));
    direction.insert("D".to_string(), (0, -1));

    let mut history: VecDeque<(i32, i32)> = VecDeque::new();
    for i in (0..n).rev() {
        history.push_back((i as i32 + 1, 0));
    }

    while q > 0 {
        input! {
            u: usize,
            v: String,
        }
        q -= 1;

        if u == 1 {
            let mut poi = history.pop_back().unwrap_or((0, 0));
            history.push_back(poi);
            if let Some(dir) = direction.get(&v) {
                poi.0 += dir.0;
                poi.1 += dir.1;
                history.push_back(poi);
            } else {
                println!("Invalid direction: {}", v);
            }
        } else if u == 2 {
            let index = v.parse::<usize>().unwrap_or(0)-1;
            if index < history.len() {
                let poi = history.iter().rev().nth(index).unwrap();
                println!("{} {}", poi.0, poi.1);
            } else {
                println!("Invalid index");
            }
        }
    }
}

