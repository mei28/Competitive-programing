use proconio::{fastout, input, marker::Chars};
use std::collections::VecDeque;

const DX: [isize; 4] = [0, 1, 0, -1];
const DY: [isize; 4] = [1, 0, -1, 0];

#[fastout]
fn main() {
    input! {h: usize, w: usize, s: [Chars; h]}

    let mut visited = vec![vec![false; w]; h];

    let mut que = VecDeque::new();
    let mut dist = vec![vec![None; w]; h];
    let mut dis: isize = -1;
    dist[0][0] = Some(0);

    que.push_back((0, 0));

    while let Some((x, y)) = que.pop_front() {
        if (x, y) == (h - 1, w - 1) {
            dis = dist[x][y].unwrap();
        }

        for i in 0..4 {
            let ny = y as isize + DY[i];
            let nx = x as isize + DX[i];

            if 0 <= nx
                && nx < h as isize
                && 0 <= ny
                && ny < w as isize
                && dist[nx as usize][ny as usize].is_none()
                && s[nx as usize][ny as usize] == '.'
            {
                que.push_back((nx as usize, ny as usize));
                dist[nx as usize][ny as usize] = Some(dist[x][y].unwrap() + 1);
            }
        }
    }

    if dis as isize == -1 {
        println!("-1");
    } else {
        let mut ans = (h * w) as isize - dis;
        for i in 0..h {
            for j in 0..w {
                if s[i][j] == '#' {
                    ans -= 1;
                }
            }
        }

        println!("{}", ans-1);
    }
}

