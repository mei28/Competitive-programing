use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize}

    for i in 1..=20 {
        let mut tmp = 1;
        for _ in 0..i {
            tmp *= i;
        }
        if tmp == n {
            println!("{}", i);
            return;
        }
    }
    println!("-1")
}
