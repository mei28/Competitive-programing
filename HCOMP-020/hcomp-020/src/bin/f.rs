use proconio::{fastout, input};
use std::cmp::Ordering;

#[fastout]
fn main() {
    input! {
        order: [usize; 10], // 0から9までの順序
        n: usize,
        mut numbers: [String; n],
    }

    let mut atcoder_order = vec![0; 10];
    for (i, &num) in order.iter().enumerate() {
        atcoder_order[num] = i;
    }

    // 順序に従って並び替え
    numbers.sort_by(|a, b| {
        let a_mapped = a.chars().map(|c| atcoder_order[c as usize - '0' as usize]);
        let b_mapped = b.chars().map(|c| atcoder_order[c as usize - '0' as usize]);

        a_mapped.cmp(b_mapped)
    });

    for number in numbers {
        println!("{}", number);
    }
}

