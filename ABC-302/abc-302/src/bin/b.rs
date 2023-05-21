use cmp::{max, min, Reverse};
use proconio::{fastout, input, marker::*};
use std::collections::*;
use std::*;

#[fastout]
fn main() {
    input! {
        h: usize,
        w: usize,
        s : [Chars;h]
    }

    let dx = vec![0, 0, -1, 1, -1, 1, -1, 1];
    let dy = vec![1, -1, 0, 0, -1, 1, 1, -1];
    for i in 0..h {
        for j in 0..w {
            for k in 0..8 {
                let mut tmp = vec![];
                let mut ans = vec![];
                for l in 0..5 {
                    let nx = i as i32 + dx[k] * l;
                    let ny = j as i32 + dy[k] * l;
                    if nx < 0 || nx >= h as i32 || ny < 0 || ny >= w as i32 {
                        break;
                    }
                    tmp.push(s[nx as usize][ny as usize]);
                    ans.push((nx+1, ny+1));
                }
                if tmp.iter().collect::<String>() == "snuke" {
                    for (u,v) in ans.iter(){
                        println!("{} {}", u, v);
                    }
                    return;
                }
            }
        }
    }
}
