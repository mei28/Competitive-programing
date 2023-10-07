use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {s:Chars}

    let result = (1..16).step_by(2).all(|i| s[i] == '0');
    if result {
        println!("Yes");
    } else {
        println!("No");
    }
}

