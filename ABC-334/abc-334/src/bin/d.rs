use proconio::{fastout, input};
use superslice::Ext;

#[fastout]
fn main() {
    input! {n:usize, mut q:usize,mut rs:[usize;n]}
    rs.sort();

    let mut accm = vec![0];

    for i in 0..n {
        accm.push(accm[i] + rs[i]);
    }
    accm.remove(0);

    while q > 0 {
        input! {x:usize};
        let idx = accm.upper_bound(&x);
        println!("{}", idx);

        q -= 1;
    }
}
