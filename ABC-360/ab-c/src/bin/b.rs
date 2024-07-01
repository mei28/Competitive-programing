use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        s: Chars,
        t: Chars,
    }

    let s_len = s.len();
    let t_len = t.len();

    for w in 1..s_len {
        for c in 1..=w {
            let mut extracted = String::new();

            for i in (c - 1..s_len).step_by(w) {
                extracted.push(s[i]);
            }

            if extracted == t.iter().collect::<String>() {
                println!("Yes");
                return;
            }
        }
    }

    println!("No");
}

