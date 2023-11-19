use proconio::{fastout, input, marker::Usize1};
use std::collections::HashMap;

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        a: [Usize1; m],
    }

    let mut vote_counts = HashMap::new();
    let mut max_votes = 0;
    let mut current_winner = 0;

    for (i, &vote) in a.iter().enumerate() {
        let count = vote_counts.entry(vote).or_insert(0);
        *count += 1;

        if *count > max_votes || (*count == max_votes && vote < current_winner) {
            max_votes = *count;
            current_winner = vote;
        }

        println!("{}", current_winner + 1);
    }
}
