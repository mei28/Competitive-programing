use proconio::{fastout, input};
use regex::Regex;

// #[fastout]
fn main() {
    input! {s:String}
    let re = Regex::new(r"^<=+>$").unwrap();

    match re.find(&s) {
        Some(_) => println!("Yes"),
        None => println!("No"),
    }
}
