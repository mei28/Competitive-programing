use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {n:usize,s: Chars}
    for i in 0..n - 1 {
        let tmp = s[i..=i + 1].iter().collect::<String>();
        if tmp == "ab" || tmp == "ba" {
            println!("Yes");
            return;
        }
    }
    println!("No");
}
