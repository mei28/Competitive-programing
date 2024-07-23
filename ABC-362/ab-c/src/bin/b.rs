use proconio::{fastout, input};

fn main() {
    input! {
        xa: f64,
        ya: f64,
        xb: f64,
        yb: f64,
        xc: f64,
        yc: f64,
    }

    let a = (xb - xc, yb - yc);
    let b = (xa - xc, ya - yc);
    let c = (xa - xb, ya - yb);

    let aa = a.0 * a.0 + a.1 * a.1;
    let bb = b.0 * b.0 + b.1 * b.1;
    let cc = c.0 * c.0 + c.1 * c.1;

    if aa + bb == cc || bb + cc == aa || cc + aa == bb {
        println!("Yes");
    } else {
        println!("No");
    }
}
