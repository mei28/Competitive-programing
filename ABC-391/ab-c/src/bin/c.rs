use proconio::input;
use std::collections::HashMap;

fn main() {
    input! {n: usize, q: usize}

    let mut pigeon_location: HashMap<usize, usize> = (1..=n).map(|i| (i, i)).collect();

    let mut nest_count = vec![1; n + 1]; // 1-based index (巣 i に最初 1 匹)

    for _ in 0..q {
        input! {t: usize}

        if t == 1 {
            input! {p: usize, h: usize}

            let old_h = pigeon_location[&p];
            pigeon_location.insert(p, h);

            nest_count[old_h] -= 1;
            nest_count[h] += 1;
        } else {
            let count = nest_count.iter().filter(|&&x| x > 1).count();
            println!("{}", count);
        }
    }
}

