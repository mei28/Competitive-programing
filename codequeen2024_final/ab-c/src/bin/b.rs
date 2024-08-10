use proconio::{fastout, input};
use std::collections::HashMap;

fn main() {
    input! {n:usize, ss:[String;n]}

    let hs: HashMap<&str, &str> = HashMap::from([
        ("-----", "0"),
        (".----", "1"),
        ("..---", "2"),
        ("...--", "3"),
        ("....-", "4"),
        (".....", "5"),
        ("-....", "6"),
        ("--...", "7"),
        ("---..", "8"),
        ("----.", "9"),
    ]);

    for s in ss.iter() {
        print!("{}", hs.get(s.as_str()).unwrap());
    }
    println!();
}
