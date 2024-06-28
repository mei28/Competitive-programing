use proconio::input;

const MOD: u64 = 998244353;

fn is_palindrome(s: &[char]) -> bool {
    let n = s.len();
    for i in 0..n / 2 {
        if s[i] != s[n - 1 - i] {
            return false;
        }
    }
    true
}

fn count_good_strings(s: &str, k: usize) -> u64 {
    let n = s.len();
    let chars: Vec<char> = s.chars().collect();
    let q_count = chars.iter().filter(|&&c| c == '?').count();
    let mut total_good_strings = 0;

    for bit in 0..(1 << q_count) {
        let mut t: Vec<char> = chars.clone();
        let mut bit_index = 0;

        for i in 0..n {
            if t[i] == '?' {
                if (bit & (1 << bit_index)) != 0 {
                    t[i] = 'B';
                } else {
                    t[i] = 'A';
                }
                bit_index += 1;
            }
        }

        let mut is_good = true;
        for i in 0..=n - k {
            if is_palindrome(&t[i..i + k]) {
                is_good = false;
                break;
            }
        }

        if is_good {
            total_good_strings += 1;
        }
    }

    total_good_strings % MOD
}

fn main() {
    input! {
        n: usize,
        k: usize,
        s: String,
    }

    let result = count_good_strings(&s, k);
    println!("{}", result);
}

