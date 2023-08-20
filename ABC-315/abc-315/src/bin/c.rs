use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, mut fs:[(usize,usize);n]}

    fs.sort_by(|a, b| b.1.cmp(&a.1));
    let mut ans = 0;

    let f = fs[0];
    for i in 1..n {
        let tmp = &fs[i];
        if tmp.0 == f.0 {
            ans = ans.max(tmp.1 / 2 + f.1);
        } else {
            ans = ans.max(f.1 + tmp.1);
        }
    }
    print!("{}", ans);
}
