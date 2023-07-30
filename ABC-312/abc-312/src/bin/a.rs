use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {s: String,}

    let v = vec!["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"];

    if v.contains(&s.as_str()) {
        println!("Yes");
    } else {
        println!("No");
    }
}
