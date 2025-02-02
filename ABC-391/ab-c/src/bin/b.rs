use proconio::input;
use proconio::marker::Chars;

fn main() {
    input! {n:usize, m:usize, s:[Chars;n], t:[Chars;m]}

    for sx in 0..n - m + 1 {
        for sy in 0..n - m + 1 {
            let mut flg = true;
            for tx in 0..m {
                for ty in 0..m {
                    if s[sx + tx][sy + ty] != t[tx][ty] {
                        flg = false;
                        break;
                    }
                }
            }

            if flg {
                println!("{} {}", sx + 1, sy + 1);
                return;
            }
        }
    }
}
