use proconio::{input, marker::Chars};

fn main() {
    input! {
        n: usize,
        k: usize,
        mut s: Chars
    }

    let mut count = 0;
    let mut i = 0;

    while i <= n - k {
        if s[i..i + k].iter().all(|&c| c == 'O') {
            s[i..i + k].iter_mut().for_each(|c| *c = 'X');
            count += 1;
            i += k;
        } else {
            i += 1;
        }
    }

    println!("{}", count);
}

