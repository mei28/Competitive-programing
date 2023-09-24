use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize, m: usize, p: usize,
        a: [usize; n],
        mut b: [usize; m],
    }

    b.sort();
    let mut accumb = vec![0; m + 1];
    for i in 0..m {
        accumb[i + 1] = b[i];
        accumb[i + 1] += accumb[i];
    }

    let mut ans = 0;

    for x in a {
        let mut ok = 0;
        let mut ng = m + 1;
        while ng - ok > 1 {
            let mid = (ok + ng) / 2;
            if b[mid - 1] + x <= p {
                ok = mid;
            } else {
                ng = mid;
            }
        }
        ans += accumb[ok] + ok * x;
        ans += p * (m - ok);
    }

    println!("{}", ans);
}

