use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
        q: usize,
        e: [(usize,usize);q],
    }

    let mut cards = vec![0; n + 1];
    for (t, x) in e {
        if t == 1 {
            cards[x] += 1;
        } else if t == 2 {
            cards[x] += 2;
        } else {
            if cards[x] >= 2 {
                println!("Yes")
            } else {
                println!("No")
            }
        }
    }
}
