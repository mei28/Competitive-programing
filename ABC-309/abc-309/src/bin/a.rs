use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {a:usize, b:usize}

    if (a - 1) / 3 == (b - 1) / 3 {
        if a + 1 == b {
            println!("Yes");
        } else {
            println!("No")
        }
    } else {
        println!("No");
    }
}
