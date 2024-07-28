use proconio::{
    fastout, input,
    marker::{Chars, Usize1},
};
use std::collections::HashMap;

fn main() {
    input! {
        h:usize,
        w:usize,
        (mut si,mut sj):( Usize1, Usize1),
        cs:[Chars;h],
        x:Chars
    }

    let mut dict = HashMap::new();
    dict.insert('U', (-1, 0));
    dict.insert('D', (1, 0));
    dict.insert('L', (0, -1));
    dict.insert('R', (0, 1));

    for a in x {
        let (di, dj) = dict[&a];

        let (nx, ny) = (si as i32 + di, sj as i32 + dj);

        if nx < 0 || ny < 0 || nx >= h as i32 || ny >= w as i32 {
            continue;
        }
        if cs[nx as usize][ny as usize] == '#' {
            continue;
        }
        si = nx as usize;
        sj = ny as usize;
    }
    println!("{} {}", si + 1, sj + 1);
}
