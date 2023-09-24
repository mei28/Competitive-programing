use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,x:usize,mut a:[usize;n-1]}

    for i in 0..=100 {
        let mut b = a.clone();
        b.insert(0, i);
        b.sort();
        let sum = b[1..n - 1].iter().sum::<usize>();
        if sum >= x {
            println!("{}", i);
            return;
        }
    }
    println!("-1");
}
