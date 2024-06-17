use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {S: String}
    let mut cnt_u = 0;
    let mut cnt_d = 0;

    for s in S.chars() {
        if s.is_ascii_lowercase() {
            cnt_d += 1;
        } else {
            cnt_u += 1;
        }
    }

    let ans = if cnt_u > cnt_d {
        S.chars().map(|c| c.to_ascii_uppercase()).collect::<String>()
    } else {
        S.chars().map(|c| c.to_ascii_lowercase()).collect::<String>()
    };
    println!("{}",ans);
}
