use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        s: Chars,
        t: Chars,
    }

    let len_s = s.len();
    let len_t = t.len();
    if len_t > len_s {
        println!("No");
        return;
    }

    for i in 0..len_s - len_t + 1 {
        let mut u = vec![];

        for j in 0..len_t {
            u.push(s[i + j]);
        }

        if u == t {
            println!("Yes");
            return;
        }
    }

    println!("No");
}
