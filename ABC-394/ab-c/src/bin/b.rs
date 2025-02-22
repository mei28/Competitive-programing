use proconio::input;

fn main() {
    input! {n:usize, mut ss:[String;n]}
    ss.sort_by(|a, b| (a.len()).cmp(&b.len()));
    let ans = ss.into_iter().collect::<String>();
    println!("{}", ans);
}
