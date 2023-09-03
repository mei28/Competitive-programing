use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize}
    let mut mat: Vec<Vec<bool>> = vec![vec![false; 101]; 101];

    for _ in 0..n {
        input! {a:usize,b:usize,c:usize,d:usize}

        for i in a..b {
            for j in c..d {
                mat[i][j] = true;
            }
        }
    }

    let ans = mat.into_iter().flatten().filter(|&x| x).count();
    println!("{}", ans);
}
