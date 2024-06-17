use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {s:String, t:String}

    let ans = match (s.as_str(), t.as_str()) {
        ("AtCoder", "Land") => "Yes",
        _ => "No",
    };
    print!("{}", ans);
}

