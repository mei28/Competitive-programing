use proconio::input;
use superslice::Ext;

fn main() {
    input! {
        n: usize,
        mut xs: [i32; n],
        ps: [i32; n],
        q: usize,
        lr: [(i32, i32); q],
    }

    // xsに対応したpsの累積和を計算する
    let mut acc = vec![0; n + 1];
    for i in 0..n {
        acc[i + 1] = acc[i] + ps[i]; // 累積和
    }

    // xsをソートする
    let mut sorted_xs = xs.clone();
    sorted_xs.sort();

    // 各範囲について累積和の計算
    for &(l, r) in &lr {
        // l以上の最初のインデックスと、r以下の最後のインデックスを二分探索で見つける
        let left = sorted_xs.lower_bound(&l);
        let right = sorted_xs.upper_bound(&r);

        // 累積和の差分で区間の合計を計算
        let sum = acc[right] - acc[left];
        println!("{}", sum);
    }
}

