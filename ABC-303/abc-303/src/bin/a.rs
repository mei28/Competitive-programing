use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
    n:usize,
    s:Chars,
    t:Chars,}

    for i in 0..n {
        let mut a = s[i];
        let mut b = t[i];

        if a == '1' {
            a = 'l';
        }

        if b == '1' {
            b = 'l';
        }
        if a == '0' {
            a = 'o';
        }

        if b == '0' {
            b = 'o';
        }

        if a != b {
            println!("No");
            return;
        }
    }

    println!("Yes");
}
