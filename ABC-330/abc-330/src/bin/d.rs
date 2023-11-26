use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        n: usize,
        ss: [Chars; n],
    }

    let mut row_counts = vec![0; n];
    let mut col_counts = vec![0; n];

    for i in 0..n {
        for j in 0..n {
            if ss[i][j] == 'o' {
                row_counts[i] += 1;
                col_counts[j] += 1;
            }
        }
    }

    let mut result = 0;

    for i in 0..n {
        for j in 0..n {
            if ss[i][j] == 'o' && row_counts[i] > 1 && col_counts[j] > 1 {
                result += (row_counts[i] - 1) as usize * (col_counts[j] - 1) as usize;
            }
        }
    }

    println!("{}", result);
}
