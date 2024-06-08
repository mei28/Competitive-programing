use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,m:usize,k:usize}
    let mut arc = vec![];
    let mut aa = vec![];
    let mut rs = vec![];
    let mut cs = vec![];

    for _ in 0..m {
        input! {c:usize,a:[usize;c],r:usize}
        arc.push((c, a.clone(), r));
        aa.push(a);
        rs.push(r);
        cs.push(c);
    }
    let mut keys = vec![0; m];
}
