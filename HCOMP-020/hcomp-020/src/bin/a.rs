use proconio::{fastout, input, marker::Usize1};
use std::collections::BTreeSet;

#[fastout]
fn main() {
    input! {n:usize,a:Usize1,b:Usize1,k:usize,ps:[Usize1;k]}
    let mut bt = BTreeSet::new();

    bt.insert(a);
    bt.insert(b);

    for i in 0..k {
        let tmp = &ps[i];
        if bt.contains(tmp) {
            println!("NO");
            return;
        }
        else{
            bt.insert(*tmp);
        }
    }
    println!("YES");
}
