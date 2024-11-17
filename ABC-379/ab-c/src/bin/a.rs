use proconio::input;

fn main() {
    input! {n: usize}

    let mut m = n;
    let c = m % 10;
    m /= 10;
    let b = m % 10;
    m /= 10;
    let a = m % 10;

    println!("{}", b * 100 + c * 10 + a);
    println!("{}", c * 100 + a * 10 + b);
}

