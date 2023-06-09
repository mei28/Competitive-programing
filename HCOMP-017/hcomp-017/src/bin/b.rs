use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {n:usize,mut x:usize,s:Chars}
    let mut t = vec![];

    for i in 0..n {
        let c = s[i];
        if c == 'U' && t.len() > 0 && (t[t.len() - 1] == 'L' || t[t.len() - 1] == 'R') {
            t.pop();
        } else {
            t.push(c);
        }
    }

    for i in 0..t.len()  {
        let c = t[i];
        if c == 'U' {
            x /= 2;
        } else if c == 'R' {
            x = 2 * x + 1;
        } else if c == 'L' {
            x = 2 * x;
        }
    }
    println!("{}", x);
}
