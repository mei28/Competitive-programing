use proconio::input;
use superslice::Ext;

fn main() {
    input! {
        n: usize,
        q: usize,
        mut aa: [isize; n],
        bk: [(isize, isize); q],
    }
    aa.sort();

    for (b, k) in bk.iter() {
        let f = |x: isize| -> bool {
            let lb = aa.lower_bound(&(b - x));
            let rb = aa.upper_bound(&(b + x));
            (rb - lb) >= *k as usize
        };

        let mut ng = -1;
        let mut ok = 200000010;
        while ok - ng > 1 {
            let mid = (ok + ng) / 2;
            if f(mid) {
                ok = mid;
            } else {
                ng = mid;
            }
        }
        println!("{}", ok);
    }
}

