use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        h: [isize; n],
    }

    let mut h = {
        let mut tmp = vec![0];
        tmp.extend(h);
        tmp.push(0);
        tmp
    };

    let mut ans = 0;
    for i in 0..=n {
        ans += (h[i + 1] - h[i]).abs();
    }
    println!("{}", ans / 2);
}

