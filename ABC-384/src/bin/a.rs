use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize}
    let ans = (1..=n)
        .map(|i| if i % 3 == 0 { 'x' } else { 'o' })
        .collect::<String>();
    println!("{}", ans);
}
