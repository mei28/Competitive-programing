use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,k:usize, mut ab:[(usize,usize);n]}

    ab.sort_by(|a, b| a.0.cmp(&b.0));

    let mut sum_b = ab.iter().fold(0, |acc, x| acc + x.1);

    let mut abc = Vec::new();
    abc.push((1, sum_b));

    for val in ab.iter() {
        let last = abc.last().unwrap();
        abc.push((val.0 + 1, last.1 - val.1));
    }

    for val in abc.iter() {
        if val.1 <= k {
            println!("{}", val.0);
            break;
        }
    }
}

