use proconio::{fastout, input};

fn check(mid: i64, aa: &[i64]) -> bool {
    let mut now = mid;
    for &a in aa {
        now += a;
        if now < 0 {
            return false;
        }
    }
    true
}

#[fastout]
fn main() {
    input! {
        n: usize,
        aa: [i64; n],
    }

    let mut ng = -1;
    // `ok` の初期値を適切に設定
    let mut ok = 1_000_000_000 * n as i64; // この値は問題の制約に基づいて調整

    while ok - ng > 1 {
        let mid = (ok + ng) / 2;
        if check(mid, &aa) {
            ok = mid;
        } else {
            ng = mid;
        }
    }

    // `ok` が最小値であることを確認
    assert!(check(ok, &aa));

    let mut ans = ok;
    for a in aa.iter() {
        ans += a;
    }
    println!("{}", ans);
}

