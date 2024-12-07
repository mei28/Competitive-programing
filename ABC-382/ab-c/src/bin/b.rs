use proconio::{input, marker::Chars};

fn main() {
    input! {n:usize, mut d:usize, mut ss:Chars}

    while d > 0 {
        for j in (0..n).rev() {
            if ss[j] == '@' {
                ss[j] = '.';
                d -= 1;
            }
            if d == 0 {
                break;
            }
        }
    }
    print!("{}", ss.iter().collect::<String>());
}
