use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {mut n: i64}
    while n % 3 == 0 {
        n /= 3;
    }
    while n % 2 == 0 {
        n /= 2;
    }

    if n == 1 {
        print!("Yes")
    } else {
        print!("No")
    }
}
