use proconio::{fastout, input};

fn main() {
    input! {n:usize,ss:[String;n]}
    if n <= 2 {
        print!("Yes");
        return;
    }

    for i in 0..n - 2 {
        if ss[i] == "sweet" && ss[i + 1] == "sweet" {
            print!("No");
            return;
        }
    }
    print!("Yes");
}
