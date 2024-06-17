use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:isize,mut m:isize,hs:[isize;n]}

    let mut idx = 0;
    for (i, h) in hs.iter().enumerate() {
        m -= h;
        if m<0{ break ;}
        idx += 1
    }

    print!("{}", idx);
}
