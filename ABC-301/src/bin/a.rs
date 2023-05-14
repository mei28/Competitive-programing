use proconio::{input, marker::Chars};

fn main() {
    input! {
        n: usize,
        S: Chars,
    }
    let mut t_cnt = 0;
    let mut a_cnt = 0;

    for i in 0..n {
        let c = S[i];
        match c {
            'T' => t_cnt += 1,
            'A' => a_cnt += 1,
            _ => unreachable!(),
        }
    }

    if t_cnt > a_cnt {
        println!("T");
    } else if t_cnt < a_cnt {
        println!("A");
    } else {
        if S[n - 1] == 'T' {
            println!("A");
        } else {
            println!("T")
        }
    }
}
