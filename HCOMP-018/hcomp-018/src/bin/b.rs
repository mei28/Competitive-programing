use proconio::{fastout, input};

const MOD: u128 = 998244353;
#[fastout]
fn main() {
    input! {n:u128}
    let mut m = 0;
    let mut nn = n;

    while nn > 0 {
        m += 1;
        nn /= 10;
    }
    let mut ans = 0;

    for i in 0..m - 1 {
        ans += ((1 + 9 * (10 as u128).pow(i as u32)) * (9 * (10 as u128).pow(i as u32)) / 2) as u128;
        ans %= MOD;
    }

    let tmp = n - (10 as u128).pow((m - 1) as u32) + 1;
    ans += (1 + tmp) * tmp / 2;
    ans %= MOD;

    println!("{}", ans);
}

