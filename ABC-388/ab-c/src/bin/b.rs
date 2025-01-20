use proconio::input;

fn main() {
    input! {n: usize, d: usize, tl: [(usize, usize); n]}

    for i in 1..=d {
        let max_value = tl.iter().map(|(t, l)| t * (l + i)).max().unwrap();
        println!("{}", max_value);
    }
}

