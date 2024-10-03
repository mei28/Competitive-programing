use proconio::{input, marker::Chars};

fn main() {
    input! { S: Chars }

    let mut positions = vec![0; 26];
    for (i, &ch) in S.iter().enumerate() {
        positions[(ch as usize - 'A' as usize)] = i as i32;
    }

    let mut current_position = positions[0]; // 最初はAの位置にいる
    let mut total_distance = 0;

    for ch in 'A'..='Z' {
        let target_position = positions[(ch as usize - 'A' as usize)];
        total_distance += (current_position - target_position).abs();
        current_position = target_position;
    }

    println!("{}", total_distance);
}

