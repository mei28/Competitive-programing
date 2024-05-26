use proconio::{fastout, input};
use std::collections::HashMap;

fn compress_coordinates(coords: &Vec<usize>) -> (Vec<usize>, HashMap<usize, usize>) {
    let mut sorted_coords = coords.clone();
    sorted_coords.sort();
    sorted_coords.dedup();

    let mut coord_map = HashMap::new();
    for (index, &coord) in sorted_coords.iter().enumerate() {
        coord_map.insert(coord, index);
    }

    let compressed_coords = coords
        .iter()
        .map(|&coord| *coord_map.get(&coord).unwrap())
        .collect();
    (compressed_coords, coord_map)
}

#[fastout]
fn main() {
    input! {
        n: usize,
        lrs: [(usize, usize); n]
    }

    let mut coords = vec![];
    for &(l, r) in &lrs {
        coords.push(l);
        coords.push(r);
    }

    let (_, coord_map) = compress_coordinates(&coords);

    let m = coord_map.len();

    let mut imos = vec![0; m + 1];

    for &(l, r) in &lrs {
        let cl = coord_map[&l];
        let cr = coord_map[&r];
        imos[cl] += 1;
        imos[cr + 1] -= 1;
    }

    for i in 1..m {
        imos[i] += imos[i - 1];
    }

    let ans = imos.iter().max().unwrap();
    print!("{}",ans);
}

