use proconio::{fastout, input};

fn divisor_count(n: usize) -> Vec<usize> {
    let mut count = vec![0; n + 1];
    for i in 1..=n {
        let mut j = i;
        while j <= n {
            count[j] += 1;
            j += i;
        }
    }
    count
}

#[fastout]
fn main() {
    input! {n:usize}

    let primes = divisor_count(n);

    let mut ans = 0;
    for k in 1..=n {
        ans += k * primes[k];
    }
    println!("{}", ans);
}

