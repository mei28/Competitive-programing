use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {t:usize}
    for _ in 0..t {
        input! {m:usize, s:[usize;m]}
        println!(
            "{}",
            s.iter().filter(|&x| x % 2 == 1).collect::<Vec<_>>().len()
        );
    }
}
