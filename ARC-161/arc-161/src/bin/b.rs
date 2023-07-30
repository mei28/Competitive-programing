use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {t:usize,ns:[usize;t]}

    for i in 0..t {
        if ns[i] < 7 {
            print!("-1");
            return;
        }
    }
}
