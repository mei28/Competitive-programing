use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {n:usize,ss:Chars}

    let mut ans = "".to_string();

    for i in (0..n).rev() {
        if ss[i] == '1' {
            // ans += 'A' * (i+1) + 'B' * i;
            ans.push_str(&"A".repeat(i + 1));
            ans.push_str(&"B".repeat(i));
        }
    }

    println!("{}", ans.len());
    println!("{}", ans);
}
