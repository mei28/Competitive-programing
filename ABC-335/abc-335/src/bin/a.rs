use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {s:Chars}

    let n = s.len();

    for i in 0..n {
        if i == n - 1 {
            print!("4");
        } else {
            print!("{}", s[i]);
        }
    }
    println!();
}
