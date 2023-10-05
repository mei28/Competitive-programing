use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {h:usize,w:usize,a:[Chars;h]}

    let mut rows = vec![false; h];
    let mut cols = vec![false; w];

    for i in 0..h {
        for j in 0..w {
            if a[i][j] == '#' {
                rows[i] = true;
                cols[j] = true;
            }
        }
    }

    for i in 0..h {
        if !rows[i] {
            continue;
        }
        for j in 0..w {
            if rows[i] && cols[j] {
                print!("{}", a[i][j]);
            }
        }
        println!("");
    }
}
