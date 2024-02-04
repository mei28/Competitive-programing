use proconio::{fastout, input, marker::Chars};
use std::collections::VecDeque;
const INF: isize = isize::MAX / 3; // To avoid overflow

#[fastout]
fn main() {
    input! {
        n: usize,
        graph: [Chars; n],
    }

    let mut dist = vec![vec![vec![vec![INF; n]; n]; n]; n];
    let dx = [-1, 0, 1, 0];
    let dy = [0, 1, 0, -1];

    let mut x1 = -1;
    let mut y1 = -1;
    let mut x2 = -1;
    let mut y2 = -1;

    // Locate the positions of the two 'P's
    for i in 0..n {
        for j in 0..n {
            if graph[i][j] == 'P' {
                if x1 == -1 {
                    x1 = i as isize;
                    y1 = j as isize;
                } else {
                    x2 = i as isize;
                    y2 = j as isize;
                }
            }
        }
    }

    let mut que = VecDeque::new();
    dist[x1 as usize][y1 as usize][x2 as usize][y2 as usize] = 0;
    que.push_back((x1, y1, x2, y2));

    while let Some((x1, y1, x2, y2)) = que.pop_front() {
        for d in 0..4 {
            let mut next1 = (x1 + dx[d], y1 + dy[d]);
            if next1.0 < 0
                || next1.0 >= n as isize
                || next1.1 < 0
                || next1.1 >= n as isize
                || graph[next1.0 as usize][next1.1 as usize] == '#'
            {
                next1 = (x1, y1); // Undo move if it's invalid or hits a wall
            }

            let mut next2 = (x2 + dx[d], y2 + dy[d]);
            if next2.0 < 0
                || next2.0 >= n as isize
                || next2.1 < 0
                || next2.1 >= n as isize
                || graph[next2.0 as usize][next2.1 as usize] == '#'
            {
                next2 = (x2, y2); // Undo move if it's invalid or hits a wall
            }

            if dist[next1.0 as usize][next1.1 as usize][next2.0 as usize][next2.1 as usize] == INF {
                dist[next1.0 as usize][next1.1 as usize][next2.0 as usize][next2.1 as usize] =
                    dist[x1 as usize][y1 as usize][x2 as usize][y2 as usize] + 1;
                que.push_back((next1.0, next1.1, next2.0, next2.1));
            }
        }
    }

    let mut ans = INF;
    for i in 0..n {
        for j in 0..n {
            ans = ans.min(dist[i][j][i][j]);
        }
    }
    if ans == INF {
        println!("-1");
    } else {
        println!("{}", ans);
    }
}

