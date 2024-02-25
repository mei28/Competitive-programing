use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {q:usize}

    let mut vec = vec![];
    for _ in 0..q {
        input! {a:usize, val:usize}
        if a == 1 {
            vec.push(val);
        } else {
            println!("{}", vec[vec.len() - val]);
        }
    }
}
