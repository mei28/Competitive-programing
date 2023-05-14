// use proconio::{fastout, input};
//
// #[fastout]
// fn main() {
//     input! {
//         n: usize,
//         a: [i32; n],
//
//     }
//
//     for i in 0..n {
//         let tmp = a[i];
//         if tmp % 2 == 0 {
//             print!("{} ", a[i]);
//         }
//     }
// }

use itertools::Itertools;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
    n: usize,
    a: [usize; n],
    }

    println!("{}", a.into_iter().filter(|x| x % 2 == 0).join(" "));
}
