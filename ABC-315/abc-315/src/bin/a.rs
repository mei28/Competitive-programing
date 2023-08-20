use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    // input! {s: String}
    // let mut result = s.replace("a", "");
    // result = result.replace("i", "");
    // result = result.replace("u", "");
    // result = result.replace("e", "");
    // result = result.replace("o", "");
    // println!("{}", result);
    input! {s: Chars}

    let result: String = s
        .iter()
        .filter(|&&c| c != 'a' && c != 'i' && c != 'u' && c != 'e' && c != 'o')
        .collect();
    println!("{}", result);
}
