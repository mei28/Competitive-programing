// use proconio::{fastout, input};
//
// #[fastout]
// fn main() {
//     input! {
//         h:usize, w:usize,
//         a: [[usize; w]; h],
//     }
//     let  v = vec!['.'].into_iter().chain('A'..='Z').collect::<Vec<_>>();
//
//     for i in 0..h {
//         for j in 0..w {
//             print!("{}", v[a[i][j]]);
//         }
//         println!();
//     }
// }

use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        h:usize, w:usize,
        a: [[usize; w]; h],
    }
    let chars = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        .to_string()
        .chars()
        .collect::<Vec<_>>();

    for i in 0..h {
        for j in 0..w {
            print!("{}", &chars[a[i][j]].to_string())
        }
        println!();
    }
}
