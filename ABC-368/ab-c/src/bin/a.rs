use proconio::input;

fn main() {
    input! {n:usize,k:usize,aa:[usize;n]}

    for i in n - k..n {
        print!("{} ", aa[i])
    }
    for i in 0..n - k {
        print!("{} ", aa[i])
    }
}
