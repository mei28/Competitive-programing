use proconio::input;

fn main() {
    input! {s:String}
    let mut chars: Vec<char> = s.chars().collect();
    chars.sort();
    let ans: bool = chars.into_iter().collect::<String>() == "ABC";
    println!("{}", if ans { "Yes" } else { "No" });
}
