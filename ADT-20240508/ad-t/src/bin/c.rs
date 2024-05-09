use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n:usize,
        m:usize,
        c: [String;n],
        d: [String;m],
        p:[usize;m+1]
    }
    // let mut ans = 0;

    // for i in c {
    //     ans += {
    //         let idx = match d.iter().position(|x| x == &i) {
    //             Some(x) => x + 1,
    //             None => 0,
    //         };
    //         p[idx]
    //     };
    // }

    let ans: usize = c
        .iter()
        .map(|i| &p[d.iter().position(|x| *x == *i).map_or(0, |idx| idx + 1)])
        .sum::<usize>();

    println!("{}", ans);
}
