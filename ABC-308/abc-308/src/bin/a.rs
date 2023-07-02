use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {s:[usize;8]}

    let mut t = s.clone();
    t.sort();

    for i in 0..8 {
        if s[i] != t[i] {
            println!("No");
            return;
        }
    }

    for i in 0..8 {
        if s[i] % 25 != 0 {
            println!("No");
            return;
        }
        if s[i] < 100 || s[i] > 675 {
            println!("No");
            return;
        }
    }
    println!("Yes");
}
