use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
       mut s: Chars,
     mut t: Chars,
    }

    let mut a = vec![true; t.len() + 1];
    let mut b = vec![true; t.len() + 1];

    for i in 0..t.len() {
        a[i + 1] &= a[i] && (s[i] == t[i] || s[i] == '?' || t[i] == '?');
    }
    s.reverse();
    t.reverse();

    for i in 0..t.len() {
        b[i + 1] &= b[i] && (s[i] == t[i] || s[i] == '?' || t[i] == '?');
    }

    s.reverse();
    t.reverse();
    b.reverse();
    for i in 0..=t.len() {
        println!("{}", if a[i] && b[i] { "Yes" } else { "No" });
    }
}
