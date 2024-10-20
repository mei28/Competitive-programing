use proconio::input;

fn main() {
    input! {
        n: usize,
        s: String,
    }

    let mut count = 0;

    if n >= 3 {
        for i in 0..n - 2 {
            if &s[i..i + 3] == "#.#" {
                count += 1;
            }
        }
    }

    println!("{}", count);
}

