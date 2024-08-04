use proconio::{fastout, input};

fn main() {
    input! {n:usize,x:usize,y:usize}
    let mut aa = vec![];
    let mut bb = vec![];

    for _ in 0..n {
        input! {a:usize,b:usize}
        aa.push(a);
        bb.push(b);
    }

    let mut dp = vec![vec![vec![1 << 20; x + 1]; n + 1]; n + 1];

    // dp_ijk: 料理1-iまでの料理で甘さの合計がjとなるようにkこの料理を選んだ時のしょっぱさの最小値
    dp[0][0][0] = 0;

    for i in 0..n {
        for j in 0..=i {
            for k in 0..=x {
                dp[i + 1][j][k] = std::cmp::min(dp[i + 1][j][k], dp[i][j][k]);
                if k + aa[i] <= x {
                    dp[i + 1][j + 1][k + aa[i]] = dp[i + 1][j + 1][k + aa[i]] =
                        std::cmp::min(
                            dp[i + 1][j + 1][k + aa[i]],
                            dp[i][j][k] + bb[i],
                        );
                }
            }
        }
    }

    for i in (0..n).rev() {
        for j in 0..=x {
            if dp[n][i][j] <= y {
                println!("{}", (i + 1).min(n));
                return 0;
            }
        }
    }
}
