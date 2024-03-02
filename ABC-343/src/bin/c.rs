use proconio::{fastout, input};

fn check(n: usize) -> bool {
    let str_n = n.to_string().chars().collect::<Vec<char>>();
    let len_n = str_n.len();

    for i in 0..len_n {
        if str_n[i] != str_n[len_n - i - 1] {
            return false;
        }
    }
    true
}

#[fastout]
fn main() {
    input! {n:usize}

    let mut ans = 1;
    let mut idx = 1;

    while idx * idx * idx <= n {
        if check(idx * idx * idx) {
            ans = idx * idx * idx;
        }
        idx += 1;
    }
    println!("{}", ans);
}
