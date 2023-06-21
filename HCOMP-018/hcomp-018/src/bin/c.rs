use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,s:String}
    let mut li = vec![];

    for i in 0..10 {
        for j in 0..10 {
            for k in 0..10 {
                li.push(format!("{}{}{}", i, j, k));
            }
        }
    }

    let mut result = 0;
    for l in &li {
        let mut idx = 0;
        for c in s.chars() {
            if Some(c) == l.chars().nth(idx) {
                idx += 1;
            }
            if idx >= 3 {
                result += 1;
                break;
            }
        }
    }
    println!("{}", result);
}

