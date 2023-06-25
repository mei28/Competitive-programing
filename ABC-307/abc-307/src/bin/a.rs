use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize}

    for _ in 0..n{
        input!{a:[usize;7]}
        println!("{}",a.iter().sum::<usize>());
    }
}
