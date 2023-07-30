use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {n:usize,m:usize,s:[Chars;n]}
    for i in 0..=n - 9 {
        for j in 0..=m - 9 {
            let mut f = true;
            for ii in i..i + 3 {
                for jj in j..j + 3 {
                    f &= s[ii][jj] == '#';
                }
            }

            for ii in i + 6..i + 9 {
                for jj in j + 6..j + 9 {
                    f &= s[ii][jj] == '#';
                }
            }
            for ii in i..i + 4 {
                f &= s[ii][j + 3] == '.';
            }
            for jj in j..j + 4 {
                f &= s[i + 3][jj] == '.';
            }
            for ii in i + 5..i + 9 {
                f &= s[ii][j + 5] == '.';
            }
            for jj in j + 5..j + 9 {
                f &= s[i + 5][jj] == '.';
            }
            if f {
                println!("{} {}", i + 1, j + 1);
            }
        }
    }
}
