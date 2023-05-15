use proconio::{fastout, input, marker::*};
fn f(c: usize, a: f64, b: f64) -> f64 {
    return c as f64 * b + a / ((c + 1) as f64).powf(0.5);
}

#[fastout]
fn main() {
    input! {
        a: f64,
        b: f64,
    }
    let mut low = 0;
    let mut high = std::usize::MAX / 100;

    loop {
        let c1 = (low * 2 + high) / 3;
        let c2 = (low + 2 * high) / 3;

        let s1 = f(c1, a, b);
        let s2 = f(c2, a, b);

        if s1 > s2 {
            low = c1;
        } else {
            high = c2;
        }

        if high - low <= 3 {
            break;
        }
    }

    let mut v = vec![];

    for i in 0..5 {
        v.push(f(low + i, a, b));
    }

    v.sort_by(|x, y| x.partial_cmp(&y).unwrap());
    println!("{}", v[0]);
}
