use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,d:usize,p:usize, mut f:[usize;n]}
    f.sort_by(|a, b| b.cmp(a));

    for i in (0..n).step_by(d) {
        let sum = (i..(i + d).min(n)).map(|x| f[x]).sum::<usize>();
        if sum > p {
            for j in i..(i + d).min(n) {
                if j == i {
                    f[j] = p;
                } else {
                    f[j] = 0;
                }
            }
        }
    }

    println!("{}", f.iter().sum::<usize>());
}
