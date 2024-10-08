use proconio::input;

fn main() {
    input! {n:usize, ks: [i64;n]}

    let mut p_ans = std::i64::MAX;
    let mut ans = 0;
    for bits in 0..(1 << n) {
        let mut a = 0;
        let mut b = 0;
        for j in 0..n {
            if bits >> j & 1 == 1 {
                a += ks[j];
            } else {
                b += ks[j];
            }
        }
        if p_ans > (a - b).abs() {
            p_ans = (a - b).abs();
            ans = a.max(b);
        }
    }
    println!("{}", ans);
}
