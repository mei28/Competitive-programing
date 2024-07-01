use proconio::{fastout, input, marker::Chars};
use regex::Regex;

#[fastout]
fn main() {
    input! {s:String}

    // let r_idx = s.iter().position(|&c| c == 'R').unwrap();
    // let m_idx = s.iter().position(|&c| c == 'M').unwrap();
    //
    // if r_idx < m_idx {
    //     println!("Yes");
    // } else {
    //     println!("No");
    // }

    let re = Regex::new(r"R.*M").unwrap();
    if re.is_match(&s) {
        println!("Yes");
    } else {
        println!("No");
    }
}
