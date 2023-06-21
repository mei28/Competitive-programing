use proconio::{fastout, input};
use rand::Rng;
// 頂点の座標を表す構造体
#[derive(Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
}

// グラフの辺を表す構造体
struct Edge {
    u: usize,
    v: usize,
    weight: i64,
}

fn convert_elements(array: &mut [u32], probability: f64) {
    let mut rng = rand::thread_rng();
    for i in 0..array.len() {
        let random_value: f64 = rng.gen();
        if random_value < probability {
            array[i] = 1;
        } else {
            array[i] = 0;
        }
    }
}

fn convert_power_elements(array: &mut [u32], probability: f64, min_val: u32, max_val: u32) {
    let mut rng = rand::thread_rng();
    for i in 0..array.len() {
        let random_value: f64 = rng.gen();
        if random_value < probability {
            array[i] = rng.gen_range(min_val, max_val);
        } else {
            array[i] = 0;
        }
    }
}
#[fastout]
fn main() {
    input! { n:usize,m:usize,k:usize}
    let mut graph = vec![];
    let mut edegs = vec![];
    let mut house = vec![];
    for _i in 0..n {
        input! {x:i64,y:i64}
        graph.push(Point { x, y });
    }
    for _i in 0..m {
        input! {u:usize,v:usize,weight:i64}
        edegs.push(Edge {
            u: u - 1,
            v: v - 1,
            weight,
        });
    }
    for _i in 0..k {
        input! {x:i64,y:i64}
        house.push(Point { x, y });
    }
    let mut bs = vec![0 as u32; n];
    let mut ps = vec![0 as u32; m];
    convert_elements(&mut ps, 1.0);
    convert_power_elements(&mut bs, 1.0, 4999,5000);
    println!(
        "{}",
        bs.iter()
            .map(|i| i.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
    println!(
        "{}",
        ps.iter()
            .map(|i| i.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
}

