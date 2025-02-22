use proconio::{input, marker::Chars};

fn main() {
    input! {s:Chars}
    let ans = s.iter().filter(|&&x| x == '2').collect::<String>();
    println!("{}", ans);
}
