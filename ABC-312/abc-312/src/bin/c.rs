use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,m:usize,a:[usize;n],b:[usize;m]}
    let mut ok = std::usize::MAX;
    let mut ng = 0;

    while ok - ng > 1 {
        let mid = (ok + ng) / 2;

        if a.iter().filter(|x| **x <= mid).count() >= b.iter().filter(|x| **x >= mid).count() {
            ok = mid
        } else {
            ng = mid
        }
    }
    println!("{}", ok);
}
