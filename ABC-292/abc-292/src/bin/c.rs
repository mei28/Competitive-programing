use proconio::{fastout, input};

pub fn gen_divisors(n: usize) -> usize {
    let mut res = vec![];

    for i in (1..).take_while(|&x| x * x <= n) {
        if n % i == 0 {
            res.push(i);
            if i * i < n {
                res.push(n / i);
            }
        }
    }

    res.sort();
    res.len()
}
#[fastout]
fn main() {
    input! {
        n: usize,
    }

    let mut ans = 0;

    for ab in 1..n  {
        let cd = n - ab;
        ans += gen_divisors(ab) * gen_divisors(cd);
    }
    println!("{}", ans);
}
