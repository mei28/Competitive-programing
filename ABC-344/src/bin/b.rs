use proconio::{fastout, input};

#[fastout]
fn main() {
    let mut ans = vec![];
    loop {
        input! {n:usize}
        ans.push(n);
        if n == 0 {
            break;
        }
    }

    for d in ans.iter().rev() {
        print!("{} ", d);
    }
}
