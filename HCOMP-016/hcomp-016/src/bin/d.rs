use proconio::{fastout, input};
use std::cmp::min;

const MOD: usize = 1_000_000_007;

#[fastout]
fn main() {
    input! {
        x: usize,
        y: usize,
    }

    for a in 0..x + 1 {
        let mut b = &x - a;
        if b % 2 == 1 {
            continue;
        }
        b /= 2;
        if 2 * a + b == y {
            println!("{}", solve(a, b));
            return;
        }
    }
    println!(0)
}

pub fn solve(a: usize, b: usize) -> usize {
    // a+b C a を求めたい
    // a+b C a = (a+b)!/(a!b!)
    // a+b C a = (a+b)!*a!^-1*b!^-1
    let (fact, inv_fact) = make_tables(a + b + 1);
    let n = a + b;
    let k = min(a, b);
    return ((fact[n] * inv_fact[k]) % MOD * inv_fact[n - k]) % MOD;
}

pub fn make_tables(n: usize) -> (Vec<usize>, Vec<usize>) {
    let mut fact = vec![1, 1];
    let mut inv_fact = vec![1, 1];
    let mut inverse = vec![0, 1];

    for i in 2..n + 1 {
        fact.push(fact[i - 1] * i % MOD);
        inverse.push(MOD - inverse[MOD % i] * (MOD / i) % MOD);
        inv_fact.push(inv_fact[i - 1] * inverse[i] % MOD);
    }
    return (fact, inv_fact);
}

/*
やりたいことは a^-1をもとめる
p = (p/a)*a + (p%a)
0 = (p/a)*a + (p%a) MOD p
0 = (p/a) + (p%a)*a^-1
a^-1 = -(p/a)*(p%a)^-1
*/
