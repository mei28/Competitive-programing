use itertools::Itertools;
use proconio::input;

fn main() {
    input! {n: usize, m: usize, aa: [usize; m]}

    let aa_set = aa.iter().collect::<std::collections::HashSet<_>>();

    let ans: Vec<_> = (1..=n)
        .filter(|i| !aa_set.contains(i))
        .collect();

    println!("{}", ans.len());
    println!("{}", ans.iter().join("\n"));
}

