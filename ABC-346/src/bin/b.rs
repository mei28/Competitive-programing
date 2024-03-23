use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {w:usize, b:usize}
    let mut piano = "wbwbwwbwbwbw".repeat(10000);
    let al = w + b;

    for i in 0..(piano.len() - al) {
        if piano[i..(i + al)].chars().filter(|&c| c == 'b').count() == b {
            println!("Yes");
            return;
        }
    }
    println!("No");
}
