use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,s:usize,k:usize,pq:[(usize,usize);n]}
    let fee = pq.iter().map(|&pq| pq.0 * pq.1).sum::<usize>();
    if fee >= s {
        println!("{}", fee);
    } else {
        println!("{}", fee + k);
    }
}
