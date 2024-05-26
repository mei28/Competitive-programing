use proconio::{fastout, input, marker::Usize1};

fn check(rows: &Vec<usize>, cols: &Vec<usize>, diag1: usize, diag2: usize, n: usize) -> bool {
    if rows.contains(&n) || cols.contains(&n) || diag1 == n || diag2 == n {
        return true;
    }
    false
}

#[fastout]
fn main() {
    input! {
        n: usize,
        t: usize,
        aa: [Usize1; t]
    }

    let mut board = vec![vec![false; n]; n];
    let mut rows = vec![0; n];
    let mut cols = vec![0; n];
    let mut diag1 = 0;
    let mut diag2 = 0;

    for (i, &a) in aa.iter().enumerate() {
        let r = a / n;
        let c = a % n;
        board[r][c] = true;
        rows[r] += 1;
        cols[c] += 1;
        if r == c {
            diag1 += 1;
        }
        if r + c == n - 1 {
            diag2 += 1;
        }
        if check(&rows, &cols, diag1, diag2, n) {
            println!("{}", i + 1);
            return;
        }
    }
    println!("-1");
}

