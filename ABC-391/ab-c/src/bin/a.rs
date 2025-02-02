use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {s:String}

    let map = HashMap::from([
        ("N", "S"),
        ("E", "W"),
        ("W", "E"),
        ("S", "N"),
        ("NE", "SW"),
        ("NW", "SE"),
        ("SE", "NW"),
        ("SW", "NE"),
    ]);

    let ans = map.get(s.as_str()).unwrap();
    println!("{}", ans);
}
