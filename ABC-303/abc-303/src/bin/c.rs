use proconio::{fastout, input, marker::Chars};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {
    n:usize,m:usize,mut h:isize,k:isize,s:Chars,xy:[(isize,isize);m],
    }

    let mut xy = xy.iter().collect::<HashSet<_>>();
    let mut p = (0, 0);
    for i in 0..n {
        let d = s[i];
        match d {
            'U' => p.1 += 1,
            'D' => p.1 -= 1,
            'R' => p.0 += 1,
            'L' => p.0 -= 1,
            _ => unreachable!(),
        }

        h -= 1;
        if h < 0 {
            println!("No");
            return;
        }
        if h < k {
            if xy.contains(&p) {
                xy.remove(&p);
                h = k;
            }
        }
    }
    println!("Yes");
}
