use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize}
    let a = n / 5;
    let b = (n + 5 - 1) / 5;

    if n - a*5 >= b*5 - n {
        println!("{}", b*5);
    } else {
        println!("{}", a*5);
    }
}
