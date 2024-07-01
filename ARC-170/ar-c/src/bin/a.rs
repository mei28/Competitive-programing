use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! { n: usize, s: Chars, t: Chars }

    let mut idx: Vec<usize> = Vec::new();
    for i in 0..n {
        if s[i] != t[i] {
            idx.push(i);
        }
    }

    if idx.is_empty() {
        println!("0");
        return;
    }

    if t[idx[0]] == 'B' {
        let mut found = false;
        for i in 0..idx[0] {
            if t[i] == 'A' {
                idx.insert(0, i);
                found = true;
                break;
            }
        }
        if !found {
            println!("-1");
            return;
        }
    }

    if t[idx[idx.len() - 1]] == 'A' {
        let mut found = false;
        for i in idx[idx.len() - 1] + 1..n {
            if t[i] == 'B' {
                idx.push(i);
                found = true;
                break;
            }
        }
        if !found {
            println!("-1");
            return;
        }
    }

    let mut res = idx.len();
    let mut ac = 0;

    for &v in &idx {
        if t[v] == 'A' {
            ac += 1;
        } else if ac > 0 {
            res -= 1;
            ac -= 1;
        }
    }

    println!("{}", res);
}

