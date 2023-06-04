use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, sa:[(String,usize);n]}

    let min_age = sa.iter().map(|x| x.1).min().unwrap();
    let min_index = sa.iter().enumerate().find(|x| x.1 .1 == min_age).unwrap().0;

    for i in 0..n {
        println!("{}", sa[(min_index + i) % n].0)
    }
}
