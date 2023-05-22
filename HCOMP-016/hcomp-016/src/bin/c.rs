use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize}
    let mut ans = [0 as isize; 200010];

    let mut x: Vec<(isize, isize)> = vec![];
    for _ in 0..n {
        input! {a:usize,b:usize}
        x.push((a as isize, 1 as isize));
        x.push(((a + b) as isize, -1));
    }
    x.sort();
    let mut cnt = 0;

    for i in 0..x.len() - 1 {
        cnt += x[i].1;
        ans[cnt as usize] += x[(i + 1)].0 as isize - x[i].0 as isize;
    }

    for i in 0..n {
        println!("{}", ans[i + 1]);
    }
}
