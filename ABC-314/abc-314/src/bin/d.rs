use itertools::Itertools;
use proconio::{
    fastout, input,
    marker::{Chars, Usize1},
};

#[fastout]
fn main() {
    input! {
        n: usize,
        mut s: Chars,
        q: usize,
        txc: [(Usize1, usize, char); q],
    }

    if txc.iter().cloned().all(|(t, _x, _c)| t == 0) {
        for (_t, x, c) in txc {
            s[x - 1] = c;
        }

        println!("{}", s.into_iter().join(""));
        return;
    }

    let m = (0..q).filter(|i| txc[*i].0 != 0).max().unwrap();

    for i in (0..q).filter(|i| txc[*i].0 == 0 || *i == m) {
        let (t, x, c) = txc[i];
        if t == 0 {
            s[x - 1] = c;
        } else if t == 1 {
            s = s
                .into_iter()
                .collect::<String>()
                .to_lowercase()
                .chars()
                .collect();
        } else {
            s = s
                .into_iter()
                .collect::<String>()
                .to_uppercase()
                .chars()
                .collect();
        }
    }

    println!("{}", s.into_iter().join(""));
}

