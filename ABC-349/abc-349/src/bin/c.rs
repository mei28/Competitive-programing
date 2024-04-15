use proconio::{fastout, input, marker::Chars};
use regex::Regex;

#[fastout]
fn main() {
    input! {
        s: String,
        t: Chars
    }

    let s = s.to_uppercase();

    let ans = (t[2] == 'X'
        && Regex::new(&format!(r".*{}.*{}", t[0], t[1]))
            .unwrap()
            .is_match(&s))
        || Regex::new(&format!(r".*{}.*{}.*{}", t[0], t[1], t[2]))
            .unwrap()
            .is_match(&s);

    if ans {
        println!("Yes");
    } else {
        println!("No");
    }
}
