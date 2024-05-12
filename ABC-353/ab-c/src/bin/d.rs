use proconio::{fastout, input};

const MOD: usize = 998244353;

#[fastout]
fn main() {
    input! {n:usize,aa:[usize;n]}
    let mut d = vec![0; 11];

    for i in 0..n {
        d[aa[i].to_string().len()] += 1;
    }

    let mut res = 0;
    let mut p10 = vec![1; 11];

    for i in 1..11 {
        p10[i] = p10[i - 1] * 10 % MOD;
    }

    for i in 0..n {
        res += aa[i] * i % MOD;
        d[aa[i].to_string().len()] -= 1;

        for j in 1..11 {
            res += p10[j] * aa[i] % MOD * d[j] % MOD;
        }
    }
    print!("{}", res % MOD);
}
