use proconio::{fastout, input};

fn prime(n: usize) -> (usize, usize) {
    for p in 2..=(n as f64).sqrt() as usize {
        if n % p == 0 {
            if n % (p * p) == 0 {
                return (p, n / (p * p));
            } else {
                return (((n / p) as f64).sqrt() as usize, p);
            }
        }
    }
    return (0, 0);
}

#[fastout]
fn main() {
    input! {
        t: usize,
    }

    for _ in 0..t {
        input! {n: usize}
        let (p, q) = prime(n);
        println!("{} {}", p, q);
    }
}

