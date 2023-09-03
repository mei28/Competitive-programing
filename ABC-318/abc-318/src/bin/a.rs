use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,mut m:usize,p:usize}
    // let mut ans = 0;
    //
    // for i in 1..=n {
    //     if i == m {
    //         ans += 1;
    //         m += p;
    //     }
    // }

    let ans = (1..=n).filter(|&x| x >= m && (x - m) % p == 0).count();
    println!("{}", ans);
}
