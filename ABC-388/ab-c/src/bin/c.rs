use proconio::input;

fn check(mid: usize, aa: &[usize]) -> bool {
    for i in 0..mid {
        let a = aa[i];
        let b = aa[i + mid];

        if a * 2 > b {
            return false;
        }
    }
    true
}

fn main() {
    input! {n:usize, aa:[usize;n]}

    let mut ok = 0;
    let mut ng = n ;

    while ng - ok > 1 {
        let mid = (ok + ng) / 2;
        println!("ok: {}, ng: {}, mid: {}", ok, ng, mid);

        if check(mid, &aa) {
            ok = mid;
        } else {
            ng = mid;
        }
    }

    println!("{}", ok);
}
