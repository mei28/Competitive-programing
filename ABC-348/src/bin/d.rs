use proconio::{fastout, input, marker::Chars};
use std::cmp::max;
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
    h:usize,
    w:usize,
    field: [Chars;h],
    n:usize,
    }

    let mut rce = vec![];
    for _ in 0..n {
        input! { r:usize,c:usize,e:usize }
        rce.push((r - 1, c - 1, e));
    }

    let mut sx: isize = -1;
    let mut sy: isize = -1;
    let mut tx: isize = -1;
    let mut ty: isize = -1;

    for i in 0..h {
        for j in 0..w {
            if field[i as usize][j as usize] == 'S' {
                sx = i as isize;
                sy = j as isize;
            }
            if field[i as usize][j as usize] == 'T' {
                tx = i as isize;
                ty = j as isize;
            }
        }
    }

    let mut s = vec![vec![-1; w]; h];

    for (r, c, e) in rce {
        s[r][c] = e as isize;
    }

    let mut dp: Vec<Vec<isize>> = vec![vec![-1 as isize; w]; h];
    dp[sx as usize][sy as usize] = 0;

    let mut que: VecDeque<(isize, isize)> = VecDeque::new();
    que.push_back((sx, sy));

    let dx = vec![0, 1, 0, -1];
    let dy = vec![1, 0, -1, 0];

    while let Some((fx, fy)) = que.pop_front() {
        let nd = max(dp[fx as usize][fy as usize], s[fx as usize][fy as usize]);
        if nd <= 0 {
            continue;
        }
        for i in 0..4 {
            let nx = fx + dx[i];
            let ny = fy + dy[i];

            if nx < 0 || nx >= h as isize || ny < 0 || ny >= w as isize || field[nx as usize][ny as usize] == '#' {
                continue;
            }

            if dp[nx as usize][ny as usize] < nd - 1 {
                dp[nx as usize][ny as usize] = nd - 1;
                que.push_back((nx, ny));
            }
        }
    }

    let bool = dp[tx as usize][ty as usize] != -1;
    println!("{}", if bool { "Yes" } else { "No" });
}
