use proconio::{input, marker::Chars};

fn main() {
    input! {
        n: usize,
        s: Chars,
        cs: [i64; n]
    }

    let mut f0 = vec![0; n + 1];
    let mut f1 = vec![0; n + 1];
    let mut g0 = vec![0; n + 1];
    let mut g1 = vec![0; n + 1];

    for i in 0..n {
        f0[i + 1] = f0[i];
        f1[i + 1] = f1[i];

        if i % 2 == 0 {
            if s[i] == '0' {
                f1[i + 1] += cs[i];
            } else {
                f0[i + 1] += cs[i];
            }
        } else {
            if s[i] == '0' {
                f0[i + 1] += cs[i];
            } else {
                f1[i + 1] += cs[i];
            }
        }
    }

    for i in (0..n).rev() {
        g0[i] = g0[i + 1];
        g1[i] = g1[i + 1];

        if i % 2 == 0 {
            if s[i] == '0' {
                g0[i] += cs[i];
            } else {
                g1[i] += cs[i];
            }
        } else {
            if s[i] == '0' {
                g1[i] += cs[i];
            } else {
                g0[i] += cs[i];
            }
        }
    }

    let mut ans = 1_000_000_000_000_000_000_i64; // 巨大な初期値

    for i in 1..n {
        ans = ans.min(f0[i] + g0[i]);
        ans = ans.min(f1[i] + g1[i]);
    }

    println!("{}", ans);
}
