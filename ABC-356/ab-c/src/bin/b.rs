use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,m:usize,aa:[usize;m],xs:[[usize;m];n]}

    // let mut ans = vec![0; m];
    //
    // for i in 0..n {
    //     for j in 0..m {
    //         ans[j] += xs[i][j];
    //     }
    // }

    let ans: Vec<usize> = (0..m).map(|j| xs.iter().map(|row| row[j]).sum()).collect();

    let flg = aa.iter().zip(ans.iter()).all(|(a, b)| a <= b);
    println!("{}", if flg { "Yes" } else { "No" });
}
