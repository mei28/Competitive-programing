use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        h: usize,
        w: usize,
        s: [Chars; h],
    }

    let mut ans = vec![vec![0; w]; h];
    let dx = vec![-1, -1, -1, 0, 0, 1, 1, 1];
    let dy = vec![-1, 0, 1, -1, 1, -1, 0, 1];

    for i in 0..h {
        for j in 0..w {
            if s[i][j] == '#' {
                ans[i][j] = -1;
                continue;
            }
            let mut cnt = 0;
            for k in 0..8 {
                let nx = i as i32 + dx[k];
                let ny = j as i32 + dy[k];
                if nx < 0 || nx >= h as i32 || ny < 0 || ny >= w as i32 {
                    continue;
                }
                if s[nx as usize][ny as usize] == '#' {
                    cnt += 1;
                }
            }
            ans[i][j] = cnt;
        }
    }

    for i in 0..h {
        for j in 0..w {
            if ans[i][j] == -1 {
                print!("#");
            } else {
                print!("{}", ans[i][j]);
            }
        }
        println!();
    }
}

