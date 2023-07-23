use core::cmp::max;
use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {n:usize, d:usize, s:[Chars;n]}

    let mut f = vec![0; d];

    for i in 0..n {
        let g = &s[i];
        for j in 0..d {
            if g[j] == 'o' {
                f[j] += 1;
            }
        }
    }
    let mut ans = 0;
    for i in 0..d {
        if f[i] == n {
            let mut j = i;

            while j < d && f[j] == n {
                j += 1;
            }
            ans = max(ans, j - i);
        }
    }
    println!("{}", ans);
}
