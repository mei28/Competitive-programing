use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, a:usize, ts:[usize;n]}

    let mut pre = 0;

    for t in ts {
        let ans = pre.max(t) + a;
        println!("{}", ans);
        pre = ans;
    }
}
