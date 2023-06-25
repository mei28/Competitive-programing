use proconio::{fastout, input, marker::Chars};

pub fn is_palindrome(s: &Vec<char>) -> bool {
    let t = s.iter().cloned().rev().collect::<Vec<_>>();
    *s == t
}

#[fastout]
fn main() {
    input! {n:usize, s: [Chars; n]}

    let mut t = vec![];

    for i in 0..n {
        for j in 0..n {
            if i == j {
                continue;
            }
            let mut u = vec![];
            for x in s[i].iter() {
                u.push(*x);
            }
            for x in s[j].iter() {
                u.push(*x);
            }
            t.push(u);
        }
    }

    println!(
        "{}",
        if t.iter().any(|x| is_palindrome(&x)) {
            "Yes"
        } else {
            "No"
        }
    );
}
