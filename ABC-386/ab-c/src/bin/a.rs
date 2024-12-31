use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {a:usize,b:usize,c:usize,d:usize}

    let mut map = HashMap::new();

    *map.entry(a).or_insert(0) += 1;
    *map.entry(b).or_insert(0) += 1;
    *map.entry(c).or_insert(0) += 1;
    *map.entry(d).or_insert(0) += 1;

    if map.len() != 2 {
        print!("No");
    } else {
        print!("Yes");
    }
}
