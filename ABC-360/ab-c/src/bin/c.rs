use proconio::{fastout, input};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        n: usize,
        aa: [usize; n],
        ws: [usize; n]
    }

    let mut map: HashMap<usize, Vec<usize>> = HashMap::new();
    for (a, w) in aa.iter().zip(ws.iter()) {
        map.entry(*a).or_insert(Vec::new()).push(*w);
    }

    let move_cost: usize = map
        .iter()
        .filter(|(_, w)| w.len() >= 2)
        .map(|(_, w)| w.iter().max().unwrap())
        .sum();

    let sum_cost: usize = map
        .iter()
        .filter(|(_, w)| w.len() >= 2)
        .map(|(_, w)| w.iter().sum::<usize>())
        .sum();

    println!("{}", sum_cost - move_cost);
}

