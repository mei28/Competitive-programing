use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize}
    let mut ans = "L".to_string();

    for _ in 0..n {
        ans.push_str("o");
    }
    ans.push_str("ng");
    println!("{}", ans);
}
