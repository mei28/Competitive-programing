use proconio::{fastout, input};
use std::cmp::{max, min};

#[fastout]
fn main() {
    input! { d: usize }

    let mut ans = d;
    let mut x = 0;

    while x * x <= d {
        let y2 = d - x * x;
        let yy = (y2 as f64).sqrt() as usize;

        for y in max(yy - 1, 0)..=(yy + 1) {
            let tmp = x * x + y * y;
            let diff = if tmp >= d { tmp - d } else { d - tmp };
            ans = min(ans, diff);
        }
        x += 1;
    }
    println!("{}", ans);
}
