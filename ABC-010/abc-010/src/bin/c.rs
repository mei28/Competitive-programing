use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        (sx, sy): (usize, usize),
        (tx, ty): (usize, usize),
        t: usize,
        v: usize,
        n: usize,
        xy: [(usize, usize); n]
    }

    for &(x, y) in &xy {
        let ds = ((sx as f64 - x as f64).powi(2) + (sy as f64 - y as f64).powi(2)).sqrt();
        let dt = ((tx as f64 - x as f64).powi(2) + (ty as f64 - y as f64).powi(2)).sqrt();
        
        if ds + dt <= (t * v) as f64 {
            println!("YES");
            return;
        }
    }
    println!("NO");
}

