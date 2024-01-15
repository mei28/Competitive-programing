use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {mut n:usize}
    n -= 1;
    let mut a = vec![];

    while n > 0 {
        a.push(n % 5);
        n /= 5;
    }

    if a.len() == 0 {
        a.push(0);
    } else {
        a.reverse();
        for i in a.iter() {
            print!("{}", i * 2);
        }
        println!();
    }
}
