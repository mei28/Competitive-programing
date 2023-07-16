use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,p:usize,q:usize,ds:[usize;n]}

    let mut ans = p;

    for d in ds {
        ans = ans.min(d + q);
    }
    println!("{}", ans);
}
