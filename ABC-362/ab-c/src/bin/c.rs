use proconio::input;

fn main() {
    input! {
        n: usize,
        lr: [(isize, isize); n],
    }

    let min_sum: isize = lr.iter().map(|&(l, _)| l).sum();
    let max_sum: isize = lr.iter().map(|&(_, r)| r).sum();

    if min_sum > 0 || max_sum < 0 {
        println!("No");
        return;
    }

    // 残りの範囲の累積和を事前に計算
    let mut remaining_min_sum = vec![0; n + 1];
    let mut remaining_max_sum = vec![0; n + 1];
    for i in (0..n).rev() {
        remaining_min_sum[i] = remaining_min_sum[i + 1] + lr[i].0;
        remaining_max_sum[i] = remaining_max_sum[i + 1] + lr[i].1;
    }

    // 解を見つける
    let mut x = vec![0; n];
    let mut current_sum = 0;

    for (i, &(l, r)) in lr.iter().enumerate() {
        let min_value = l.max(-current_sum - remaining_max_sum[i + 1]);
        let max_value = r.min(-current_sum - remaining_min_sum[i + 1]);

        if min_value <= max_value {
            x[i] = min_value;
        } else {
            x[i] = l;
        }
        current_sum += x[i];
    }

    println!("Yes");
    for xi in x {
        print!("{} ", xi);
    }
    println!();
}
