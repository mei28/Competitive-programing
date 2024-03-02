use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize}

    for _ in 0..n {
        input! {aa:[usize;n]}

        for (i, a) in aa.iter().enumerate() {
            if *a == 1 {
                print!("{} ", i + 1);
            }
        }
        println!()
    }
}
