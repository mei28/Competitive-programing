use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, mut ac:[(usize, usize);n]}

    ac.sort_by(|a, b| a.0.cmp(&b.0).then(b.1.cmp(&a.1)));
    println!("{:?}", ac);
}
