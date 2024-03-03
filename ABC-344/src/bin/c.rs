use proconio::{fastout, input};
use std::collections::HashSet;

#[fastout]
fn main() {
    input! {n:usize, a:[usize;n], m:usize, b:[usize;m], l:usize, c:[usize;l], q:usize, x:[usize;q]};

    let mut set = HashSet::new();
    for aa in a.iter() {
        for bb in b.iter() {
            for cc in c.iter() {
                set.insert(aa + bb + cc);
            }
        }
    }

    for xx in x.iter() {
        if set.contains(xx) {
            println!("Yes");
        } else {
            println!("No");
        }
    }
}
