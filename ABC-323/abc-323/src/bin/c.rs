use proconio::{fastout, input, marker::Chars};
use std::cmp::max;

#[fastout]
fn main() {
    input! {n:usize,m:usize,a:[usize;m] ,ss:[Chars;n]}

    let mut scores = vec![0; n];
    let mut max_score = 0;

    for i in 0..n {
        for j in 0..m {
            if ss[i][j] == 'o' {
                scores[i] += a[j];
            }
        }
        scores[i] += i + 1;
        max_score = max(max_score, scores[i]);
    }

    for i in 0..n {
        let mut remaining_problems = vec![];
        for j in 0..m {
            if ss[i][j] == 'x' {
                remaining_problems.push(a[j]);
            }
        }

        remaining_problems.sort_by(|a, b| b.cmp(&a));

        let mut additional_score = scores[i];
        let mut count = 0;
        for score in &remaining_problems {

            if additional_score >= max_score {
                break;
            }
            additional_score += score;
            count += 1;
        }
        println!("{}", count);
    }
}
