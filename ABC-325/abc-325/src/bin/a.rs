use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {S: Chars, _T: Chars}
    println!("{} san", S.iter().collect::<String>());
}
