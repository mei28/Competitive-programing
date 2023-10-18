use proconio::{input, source::line::LineSource};
use rand::seq::SliceRandom;
use rand::Rng;
use std::io::{self, stdin, stdout, BufReader, Write};

#[derive(Debug, Copy, Clone)]
struct Item {
    weight: i32,
    group: usize,
}

fn select_samples(items: &Vec<Item>, indices: &mut Vec<usize>, k: usize) -> Vec<usize> {
    indices.sort_by_key(|&index| items[index].weight);

    let actual_k = std::cmp::min(k, indices.len() / 2); // 実際に使用するkの値

    let top_k_lightest = indices
        .iter()
        .take(actual_k)
        .cloned()
        .collect::<Vec<usize>>();
    let top_k_heaviest = indices
        .iter()
        .rev()
        .take(actual_k)
        .cloned()
        .collect::<Vec<usize>>();

    [top_k_lightest, top_k_heaviest].concat()
}

fn query(
    left_group: usize,
    right_group: usize,
    items: &Vec<Item>,
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
    // 最軽と推定されるアイテムと最重と推定されるアイテムを選択
    left.sort_by_key(|&index| items[index].weight);
    right.sort_by_key(|&index| items[index].weight);
    let k = 3; // 例としてkを3に設定
    let left_samples = select_samples(&items, &mut left, k);
    let right_samples = select_samples(&items, &mut right, k);

    // クエリを投げる
    println!(
        "{} {} {} {}",
        left_samples.len(),
        right_samples.len(),
        left_samples
            .iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join(" "),
        right_samples
            .iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join(" ")
    );

    *query_count += 1;
    io::stdout().flush().unwrap();

    let mut stdin = LineSource::new(BufReader::new(io::stdin()));
    macro_rules! input(($($tt:tt)*) => (proconio::input!(from &mut stdin, $($tt)*)));
    input! {c:char}
    (c, left_samples, right_samples)
}

fn show_ans(items: &Vec<Item>, debug: bool) {
    let answer: Vec<String> = items.iter().map(|item| item.group.to_string()).collect();
    if debug {
        print!("#c ");
    }
    println!("{}", answer.join(" "));
    io::stdout().flush().unwrap();
}

fn swap_specific_items(
    left_indices: &Vec<usize>,
    right_indices: &Vec<usize>,
    items: &mut Vec<Item>,
) {
    let left_group = items[left_indices[0]].group; // 左側のアイテムのグループを取得
    let right_group = items[right_indices[0]].group; // 右側のアイテムのグループを取得

    // 左側のアイテムのグループを右側のアイテムのグループに更新
    for &index in left_indices.iter() {
        items[index].group = right_group;
    }

    // 右側のアイテムのグループを左側のアイテムのグループに更新
    for &index in right_indices.iter() {
        items[index].group = left_group;
    }
}

fn reassign_groups_based_on_weight(items: &mut Vec<Item>, d: usize) {
    let mut indexed_weights: Vec<(i32, usize)> = items
        .iter()
        .enumerate()
        .map(|(idx, item)| (item.weight, idx))
        .collect();
    indexed_weights.sort_by(|a, b| a.0.cmp(&b.0));

    // 各グループの合計重さを格納
    let mut group_sums: Vec<i32> = vec![0; d];

    // ソートされたアイテムのリストを逆順にイテレート
    for (_, original_idx) in indexed_weights.iter().rev() {
        // 現在のアイテムを最も軽いグループに割り当て
        let min_group_idx = group_sums
            .iter()
            .enumerate()
            .min_by_key(|&(_, sum)| sum)
            .unwrap()
            .0;
        items[*original_idx].group = min_group_idx;
        group_sums[min_group_idx] += items[*original_idx].weight;
    }
}
fn main() {
    let mut stdin = LineSource::new(BufReader::new(io::stdin()));
    macro_rules! input(($($tt:tt)*) => (proconio::input!(from &mut stdin, $($tt)*)));
    input! {n:usize,d:usize,q:usize}

    let mut items = Vec::with_capacity(n);
    for i in 0..n {
        items.push(Item {
            weight: 0,
            group: i % d,
        });
    }
    let mut query_count = 0;
    while query_count < q {
        let mut rng = rand::thread_rng();
        let group_a: usize = rng.gen_range(0..d);
        let mut group_b: usize;
        loop {
            group_b = rng.gen_range(0..d);
            if group_a != group_b {
                break;
            }
        }
        let (ans1, selected_left_1, selected_right_1) =
            query(group_a, group_b, &items, &mut query_count);

        if selected_left_1.len() >= 2 && selected_right_1.len() >= 2 {
            if ans1 == '<' {
                items[selected_left_1[0]].weight -= 1;
                items[selected_left_1[1]].weight += 1;
                items[selected_right_1[0]].weight += 1;
                items[selected_right_1[1]].weight -= 1;

                swap_specific_items(&selected_left_1, &selected_right_1, &mut items);
            } else {
                items[selected_left_1[0]].weight += 1;
                items[selected_left_1[1]].weight -= 1;
                items[selected_right_1[0]].weight -= 1;
                items[selected_right_1[1]].weight += 1;

                swap_specific_items(&selected_right_1, &selected_left_1, &mut items);
            }
        }
    }

    // reassign_groups_based_on_weight(&mut items, d);
    show_ans(&items, false);
}

