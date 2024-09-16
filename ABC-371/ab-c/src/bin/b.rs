use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {n:usize, m:usize, ab:[(usize,char);m]}

    let mut set: HashSet<usize> = HashSet::new();

    for (a, b) in ab {
        if b != 'M' {
            println!("No");
            continue;
        }

        if set.contains(&a) {
            println!("No");
        } else {
            set.insert(a);
            println!("Yes");
        }
    }
}
