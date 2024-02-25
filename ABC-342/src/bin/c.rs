use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        n: usize,
        s: Chars,
        q: usize,
        cd: [(char, char); q],
    }

    let mut from: Vec<char> = "abcdefghijklmnopqrstuvwxyz".chars().collect();
    let mut to: Vec<char> = from.clone();

    for (c, d) in cd {
        for m in to.iter_mut() {
            if *m == c {
                *m = d;
            }
        }
    }

    for c in s {
        if let Some(pos) = from.iter().position(|&x| x == c) {
            print!("{}", to[pos]);
        }
    }
    println!();
}
