use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize, xy:[(usize,usize);n]}

    // let mut left = 0;
    // let mut right = 0;

    // for (x, y) in xy.iter() {
    //     left += x;
    //     right += y;
    // }

    let left = xy.iter().map(|(x, _)| x).sum::<usize>();
    let right = xy.iter().map(|(_, y)| y).sum::<usize>();

    println!(
        "{}",
        if left == right {
            "Draw"
        } else {
            if left > right {
                "Takahashi"
            } else {
                "Aoki"
            }
        }
    );
}
