use proconio::{fastout, input};
use regex::Regex;

#[fastout]
fn main() {
    input! {s:String}

    let ans = Regex::new(r"^<=*>$").unwrap().is_match(&s);
    print!("{}", if ans { "Yes" } else { "No" });
}
