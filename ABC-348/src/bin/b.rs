use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,xy:[(isize,isize);n]}

    for i in 0..n {
        let mut dist = 0;
        let (xi, yi) = xy[i];
        let mut tmp = i;
        for j in 0..n {
            let (xj, yj) = xy[j];

            let diff = (xi - xj).pow(2) + (yi - yj).pow(2);

            if diff > dist {
                dist = diff;
                tmp = j;
            }
        }
        println!("{}", tmp + 1);
    }
}
