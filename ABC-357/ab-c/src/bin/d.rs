use proconio::{fastout, input};

const MOD: i64 = 998244353;

#[fastout]
fn main() {
    input! { n: i64 }
    println!("{}", f(n, n));
}

fn f(n: i64, i: i64) -> i64 {
    if i == 1 {
        return n % MOD;
    }
    let k = n.to_string().len() as u32;
    if i % 2 == 0 {
        let t = f(n, i / 2);
        return (t * mod_pow(10, (i / 2) * k as i64, MOD)) % MOD;
    } else {
        return (f(n, i - 1) * mod_pow(10, k as i64, MOD) + n) % MOD;
    }
}

fn mod_pow(base: i64, exp: i64, modulus: i64) -> i64 {
    let mut result = 1;
    let mut base = base % modulus;
    let mut exp = exp;
    while exp > 0 {
        if exp % 2 == 1 {
            result = result * base % modulus;
        }
        base = base * base % modulus;
        exp /= 2;
    }
    result
}

