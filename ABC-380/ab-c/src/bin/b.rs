use proconio::{input, marker::Chars};

fn main() {
    input! {S: Chars}

    let mut cnt = 0;

    for i in 1..S.len() {
        if S[i - 1] == '-' {
            cnt += 1;
        } else {
            if cnt != 0 {
                print!("{} ", cnt);
            }
            cnt = 0;
        }
    }
    if cnt != 0 {
        print!("{}", cnt);
    }
}
