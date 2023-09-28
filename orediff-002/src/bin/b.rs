use proconio::{fastout, input};
use std::mem::swap;

#[fastout]
fn main() {
    input! {q:usize}
    let n = 1 << 20;
    let mut p = vec![-1; n + 1];
    let mut a = vec![-1; n];

    for _ in 0..q {
        input! {t:usize,x:usize}
        if t == 1 {
            let h = x % n;
            let mut target = root(h, &mut p);
            if target == n {
                target = root(0, &mut p);
            }
            a[target] = x as isize;
            merge(target, target + 1, &mut p);
        } else {
            println!("{}", a[x % n]);
        }
    }
}

fn root(x: usize, p: &mut Vec<isize>) -> usize {
    if p[x] < 0 {
        return x;
    } else {
        p[x] = root(p[x] as usize, p) as isize;
    }
    return p[x] as usize;
}

fn merge(x: usize, mut y: usize, p: &mut Vec<isize>) -> bool {
    let mut x = root(x, p);
    let mut y = root(y, p);
    if x == y {
        return false;
    }
    if x < y {
        swap(&mut x, &mut y);
    }

    p[x] += p[y];
    p[y] = x as isize;
    return true;
}
