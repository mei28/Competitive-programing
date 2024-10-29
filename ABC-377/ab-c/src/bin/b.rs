use proconio::{input, marker::Chars};

fn main() {
    input! {table: [Chars;8]}

    let x_num = table
        .iter()
        .enumerate()
        .filter(|(_, row)| row.iter().any(|&c| c == '#'))
        .count();

    let y_num = (0..8)
        .filter(|i| table.iter().any(|row| row[*i] == '#'))
        .count();

    print!("{}", (8 - x_num) * (8 - y_num));
}
