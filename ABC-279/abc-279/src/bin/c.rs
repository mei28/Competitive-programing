use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        h: usize, w: usize,
        s: [Chars; h],
        t: [Chars; h],
    }

    let mut ss = vec![];
    let mut tt = vec![];
    for j in 0..w {
        let mut add_s = vec![];
        let mut add_t = vec![];
        for i in 0..h {
            add_s.push(s[i][j]);
            add_t.push(t[i][j]);
        }
        ss.push(add_s);
        tt.push(add_t);
    }

    ss.sort();
    tt.sort();

    println!("{}", if ss == tt { "Yes" } else { "No" });
}
