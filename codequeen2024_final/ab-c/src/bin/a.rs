use proconio::{fastout, input};

fn main() {
    input! {x:usize}

    if x <= 10 {
        println!("10")
    } else if x <= 15 {
        println!("15")
    } else {
        println!("17")
    }
}
