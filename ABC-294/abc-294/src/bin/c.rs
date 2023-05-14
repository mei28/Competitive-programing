use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        n:usize,
        m:usize,
        a:[usize;n],
        b:[usize;m],
    }
    let mut c = a
        .iter()
        .cloned()
        .chain(b.iter().cloned())
        .collect::<Vec<_>>();
    c.sort();

    let mut map = HashMap::new();

    for i in 0..n + m {
        map.insert(c[i], i + 1);
    }


    for x in a.into_iter(){
        print!("{} ", map[&x]);
    }
    println!();
    for x in b.into_iter(){
        print!("{} ", map[&x]);
    }
}
