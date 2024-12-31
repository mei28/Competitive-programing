use proconio::input;

fn main() {
    input! {
        n: u64, // N 以下の正整数
    }

    // エラトステネスの篩で素数リストを作成
    let limit = (n as f64).sqrt().ceil() as u64 + 1;
    let mut is_prime = vec![true; limit as usize];
    let mut primes = vec![];

    is_prime[0] = false;
    is_prime[1] = false;

    for i in 2..limit {
        if is_prime[i as usize] {
            primes.push(i);
            let mut multiple = i * i;
            while multiple < limit {
                is_prime[multiple as usize] = false;
                multiple += i;
            }
        }
    }

    let mut count = 0;

    // ケース 1: p^8
    for &p in &primes {
        // 安全に p^8 を計算
        let mut power = Some(p);
        for _ in 0..7 {
            power = power.and_then(|x| x.checked_mul(p)); // オーバーフローをチェックしながら掛け算
        }
        if let Some(power) = power {
            if power <= n {
                count += 1;
                // println!("p^8: {}", power);
            }
        }
    }

    // ケース 2: p^2 * q^2
    let primes_len = primes.len();
    for i in 0..primes_len {
        let p2 = primes[i] * primes[i];
        if p2 > n {
            break;
        }
        for j in (i + 1)..primes_len {
            let q2 = primes[j] * primes[j];
            if p2 > n / q2 {
                break;
            }
            let num = p2 * q2;
            if num <= n {
                count += 1;
                // println!("p^2 * q^2: {}", num);
            }
        }
    }

    println!("{}", count);
}

