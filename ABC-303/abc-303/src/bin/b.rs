use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, m:usize, a: [[usize; n]; m]}
    let mut flg = vec![vec![false; n]; n];

    for i in 0..m {
        for j in 0..n - 1 {
            let left = a[i][j] - 1;
            let right = a[i][j + 1] - 1;
            flg[left][right] = true;
            flg[right][left] = true;
        }
    }
    let mut cnt = 0;
    for i in 0..n - 1 {
        for j in i + 1..n {
            if !flg[i][j] {
                cnt += 1;
            }
        }
    }
    println!("{}", cnt );
}
