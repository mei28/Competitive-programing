use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, aa:[usize;n*2]}

    let mut ans = 0;

    for i in 1..=n {
        let mut left = -1;
        let mut right = -1;

        for j in 0..n * 2 {
            if aa[j] == i {
                if left == -1 {
                    left = j as isize;
                } else {
                    right = j as isize;
                    break;
                }
            }
        }

        if right - left == 2 {
            ans += 1;
        }
    }
    println!("{}", ans);
}
