use proconio::{input, marker::Chars};

fn main() {
    input! {h:usize,w:usize,ss:[Chars;h]}

    for s in ss {
        let ans = s.iter().collect::<String>().replace("TT", "PC");
        println!("{}", ans)
    }
}
