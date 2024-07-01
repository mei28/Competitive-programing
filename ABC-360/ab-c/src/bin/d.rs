use itertools::Itertools;
use proconio::{fastout, input, marker::Chars};

pub trait BinarySearch<T> {
    fn lower_bound(&self, key: T) -> usize;
    fn upper_bound(&self, key: T) -> usize;
}

impl<T> BinarySearch<T> for [T]
where
    T: Ord,
{
    fn lower_bound(&self, key: T) -> usize {
        let mut ng = -1isize;
        let mut ok = self.len() as isize;
        while ok - ng > 1 {
            let mid = (ok + ng) / 2;
            if key <= self[mid as usize] {
                ok = mid;
            } else {
                ng = mid;
            }
        }
        ok as usize
    }

    fn upper_bound(&self, key: T) -> usize {
        let mut ng = -1isize;
        let mut ok = self.len() as isize;
        while ok - ng > 1 {
            let mid = (ok + ng) / 2;
            if key < self[mid as usize] {
                ok = mid;
            } else {
                ng = mid;
            }
        }
        ok as usize
    }
}

#[fastout]
fn main() {
    input! {
        n: usize,
        t: isize,
        s: Chars,
        xs: [isize; n]
    }

    let right = xs
        .iter()
        .zip(s.iter())
        .filter(|(_, &d)| d == '1')
        .map(|(&x, _)| x)
        .sorted()
        .collect::<Vec<_>>();

    let left = xs
        .iter()
        .zip(s.iter())
        .filter(|(_, &d)| d == '0')
        .map(|(&x, _)| x)
        .sorted()
        .collect::<Vec<_>>();

    let mut ans = 0;
    for &r in &right {
        let le = left.lower_bound(r);
        let ri = left.upper_bound(r + 2 * t);
        ans += ri - le;
    }
    println!("{}", ans);
}

