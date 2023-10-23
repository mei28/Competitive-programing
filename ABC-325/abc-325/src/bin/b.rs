use proconio::{fastout, input};
use std::cmp::max;

#[fastout]
fn main() {
    input! {n:usize, wx:[(usize, usize); n]}

    let mut ans = 0;
    for i in 0..24 {
        let mut cnt = 0;

        for (w, x) in &wx {
            let start_time = (i + x) % 24;
            let end_time = (start_time + 1) % 24;
            if (9 <= start_time && start_time < 18) && (9 <= end_time && end_time <= 18) {
                cnt += w;
            }
        }

        ans = max(ans, cnt);
    }
    println!("{}", ans);
}

