use proconio::{fastout, input};

// (x+A_i - min(A_i,2*x))
// Nx+\Sigma A_i - min(A_i,2*x))

#[fastout]
fn main() {
    input! {n:usize, a: [f64;n]}
    let cal = |x: f64| -> f64 { a.iter().map(|&ai| x.max(ai - x)).sum::<f64>() };
    let mut l = 0_f64;
    let mut r = 1e18_f64;
    let phi = (5_f64.sqrt() + 1_f64) / 2_f64;
    for _ in 0..200 {
        let x = [(l * phi + r) / (1_f64 + phi), (l + phi * r) / (1_f64 + phi)];

        if cal(x[0]) < cal(x[1]) {
            r = x[1];
        } else {
            l = x[0];
        }
    }
    let ans = cal(l) / n as f64;
    println!("{}", ans);
}
