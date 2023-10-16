use proconio::{input, source::line::LineSource};
use rand::seq::SliceRandom;
use rand::Rng;
use std::io::{self, stdin, stdout, BufReader, Write};

#[derive(Debug, Copy, Clone)]
struct Item {
    weight: i32,
    group: usize, // アイテムがどのグループに属しているか
}

fn query(
    left_group: usize,
    right_group: usize,
    items: &Vec<Item>,
    flg: bool,
    query_count: &mut usize,
) -> (char, Vec<usize>, Vec<usize>) {
    let mut left: Vec<usize> = items
        .iter()
        .enumerate()
        .filter(|&(_, item)| item.group == left_group)
        .map(|(index, _)| index)
        .collect();
    let mut right: Vec<usize> = items
        .iter()
        .enumerate()
        .filter(|&(_, item)| item.group == right_group)
        .map(|(index, _)| index)
        .collect();
    if flg {
        left = select_random_percentage(&left, 0.2);
        right = select_random_percentage(&right, 0.2);
    }

    // クエリを投げる
    println!(
        "{} {} {} {}",
        left.len(),
        right.len(),
        left.iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join(" "),
        right
            .iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join(" ")
    );
    *query_count += 1;
    // 出力をフラッシュする
    io::stdout().flush().unwrap();

    let mut stdin = LineSource::new(BufReader::new(io::stdin()));
    macro_rules! input(($($tt:tt)*) => (proconio::input!(from &mut stdin, $($tt)*)));
    // 結果を受け取る
    input! {c:char}
    (c, left, right) // 選択された左側と右側のアイテムのインデックスも返します
}

fn swap_specific_items(
    left_indices: &Vec<usize>,
    right_indices: &Vec<usize>,
    items: &mut Vec<Item>,
) {
    for &index in left_indices.iter() {
        items[index].group = items[right_indices[0]].group;
    }
    for &index in right_indices.iter() {
        items[index].group = items[left_indices[0]].group;
    }
}

fn select_random_percentage<T: Clone>(items: &Vec<T>, percentage: f32) -> Vec<T> {
    let count = (items.len() as f32 * percentage).ceil() as usize;
    items
        .choose_multiple(&mut rand::thread_rng(), count)
        .cloned()
        .collect()
}

fn show_ans(items: &Vec<Item>, debug: bool) {
    let answer: Vec<String> = items.iter().map(|item| item.group.to_string()).collect();
    if debug {
        print!("#c ");
    }
    println!("{}", answer.join(" "));
    // 出力をフラッシュする
    io::stdout().flush().unwrap();
}

fn main() {
    let mut stdin = LineSource::new(BufReader::new(io::stdin()));
    macro_rules! input(($($tt:tt)*) => (proconio::input!(from &mut stdin, $($tt)*)));
    input! {n:usize,d:usize,q:usize}

    let mut items = Vec::with_capacity(n);
    for i in 0..n {
        items.push(Item {
            weight: -1,
            group: i % d, // これにより、各アイテムは 0 から d-1 までの異なるグループIDを持ちます
        });
    }
    let mut query_count = 0;
    let mut ans1 = '='; // 初期値を設定
    let mut selected_left = Vec::new();
    let mut selected_right = Vec::new();
    while query_count < q {
        show_ans(&items, true);
        let group_a = query_count % d;
        let group_b = (query_count + 1) % d;

        (ans1, selected_left, selected_right) =
            query(group_a, group_b, &items, true, &mut query_count);
        swap_specific_items(&selected_left, &selected_right, &mut items);
    }

    // TODO: 分割した答えを投げる
    show_ans(&items, false);
}
