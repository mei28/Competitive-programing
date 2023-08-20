use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {m:usize, ds : [usize; m]}
    let ave = (ds.iter().sum::<usize>()) / 2;

    let mut sum = 0;
    for i in 0..m {
        let tmp = ds[i];
        if sum + tmp > ave {
            print!("{} {}", i + 1, ave - sum + 1);
            return;
        }
        sum += tmp;
    }
}
