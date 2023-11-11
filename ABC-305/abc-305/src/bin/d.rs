use proconio::input;

pub trait BinarySearch<T> {
    fn lower_bound(&self, key: T) -> usize;
    fn upper_bound(&self, key: T) -> usize;
}

impl<T> BinarySearch<T> for [T]
where
    T: Ord,
{
    fn lower_bound(&self, key: T) -> usize {
        let mut ng = -1 as isize;
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
        let mut ng = -1 as isize;
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

fn f(x: usize, a: &[usize], fa: &[usize]) -> usize {
    let j = a.upper_bound(x) - 1;
    fa[j]
        + if a[j] < x && j + 1 < a.len() {
            (fa[j + 1] - fa[j]) / (a[j + 1] - a[j]) * (x - a[j])
        } else {
            0
        }
}

fn main() {
    input! {
        n: usize,
        a: [usize; n],
        q: usize,
        lr: [(usize, usize); q],
    }

    let mut fa = vec![0; n];

    // fA の計算
    for i in 1..n {
        fa[i] = fa[i - 1] + if i % 2 == 0 { a[i] - a[i - 1] } else { 0 };
    }

    // クエリの処理
    for &(l, r) in &lr {
        println!("{}", f(r, &a, &fa) - f(l, &a, &fa));
    }
}
