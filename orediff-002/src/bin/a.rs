use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,ps:[usize; n],qs:[usize; n]}
    let mut p = ps.clone();
    let mut q = qs.clone();
    p.sort();
    q.sort();
    let mut p_index = 0;
    let mut q_index = 0;
    for (index, permutation) in p.into_iter().permutations(n).enumerate() {
        if permutation == ps {
            p_index = index;
        }
    }

    for (index, permutation) in q.into_iter().permutations(n).enumerate() {
        if permutation == qs {
            q_index = index;
        }
    }

    println!("{}", (p_index as isize - q_index as isize).abs());
}
