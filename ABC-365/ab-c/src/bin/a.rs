use proconio::{fastout, input};

fn main() {
    input! {y:usize}
    let ans = if check_uruu(y) { 366 } else { 365 };
    println!("{}", ans);
}

fn check_uruu(y: usize) -> bool {
    if y % 400 == 0 {
        return true;
    }
    if y % 100 == 0 {
        return false;
    }
    if y % 4 == 0 {
        return true;
    }
    false
}
