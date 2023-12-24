use proconio::input;

fn floor(x: i64, m: i64) -> i64 {
    let r = (x % m + m) % m;
    return (x - r) / m;
}

fn main() {
    input! { a: i64, m: i64, mut        l: i64, mut      r: i64, }
    l -= a;
    r -= a;
    println!("{}", floor(r, m) - floor(l - 1, m));
}
