use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {n:usize, mut s:[Chars;n]}
    let mut v = vec![];

    for i in 0..n {
        let wins = s[i].iter().filter(|&&c| c == 'o').count();
        v.push((wins, i));
    }
    v.sort_by(|a, b| b.0.cmp(&a.0).then(a.1.cmp(&b.1)));
    for (_, i) in v {
        println!("{}", i + 1);
    }
}
