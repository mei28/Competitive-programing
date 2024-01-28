use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {s:Chars}

    if s[0].is_ascii_uppercase() && s.iter().skip(1).all(|c| c.is_ascii_lowercase()) {
        println!("Yes");
    } else {
        println!("No");
    }
}
