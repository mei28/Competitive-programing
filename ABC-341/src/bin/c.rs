use proconio::{fastout, input, marker::Chars};
use std::collections::HashMap;

fn check(
    x: isize,
    y: isize,
    h: isize,
    w: isize,
    ts: &Vec<char>,
    ss: &Vec<Vec<char>>,
    dict: &HashMap<char, (isize, isize)>,
) -> bool {
    let mut nx = x;
    let mut ny = y;

    if ss[nx as usize][ny as usize] == '#' {
        return false;
    }
    for m in ts.iter() {
        let (dx, dy) = dict.get(m).unwrap();
        nx += dx;
        ny += dy;

        if nx < 0 || nx >= h || ny < 0 || ny >= w {
            return false;
        }
        if ss[nx as usize][ny as usize] == '#' {
            return false;
        }
    }
    true
}

#[fastout]
fn main() {
    input! {h:isize,w:isize,n:isize}
    let dict = HashMap::from([('L', (0, -1)), ('R', (0, 1)), ('U', (-1, 0)), ('D', (1, 0))]);
    input! {ts: Chars}
    input! {ss: [ Chars ;h]}

    let mut ans = 0;
    for i in 0..h {
        for j in 0..w {
            if check(i, j, h, w, &ts, &ss, &dict) {
                ans += 1;
            }
        }
    }
    println!("{}", ans);
}
