use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {mut a:usize}

    if a < 10 {
        println!("Yes");
        return;
    } else {
        let mut d = a % 10;
        a /= 10;

        while a > 0 {
            if a % 10 > d {
                d = a % 10;
                a /= 10;
            } else {
                println!("No");
                return;
            }
        }
        println!("Yes");
    }
}
