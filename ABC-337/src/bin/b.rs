use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {s: Chars};

    let mut now = 0;

    for i in s.iter() {
        let tar = match *i {
            'A' => 0,
            'B' => 1,
            'C' => 2,
            _ => panic!(),
        };

        if tar < now {
            println!("No");
            return;
        } else {
            now = tar;
        }
    }
    println!("Yes");
}
