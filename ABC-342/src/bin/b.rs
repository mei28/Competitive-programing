use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, ps: [usize;n], q:usize, ab:[(usize,usize);q]}

    for (a, b) in ab {
        let idx_a = ps.iter().position(|&x| x == a).unwrap();
        let idx_b = ps.iter().position(|&x| x == b).unwrap();

        if idx_a < idx_b {
            println!("{}", a);
        } else {
            println!("{}", b);
        }
    }
}
