use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {s: Chars}
    for i in s.iter() {
        print!("{} ", i)
    }
}
