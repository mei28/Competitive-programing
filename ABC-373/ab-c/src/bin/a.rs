use proconio::input;

fn main() {
    input! {ss: [String;12]}

    let ans = ss
        .iter()
        .enumerate()
        .filter(|(i, s)| s.len() == i + 1)
        .count();
    println!("{}", ans);
}
