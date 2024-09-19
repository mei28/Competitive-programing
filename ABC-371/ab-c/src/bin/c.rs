use permutohedron::LexicalPermutation;
use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {n:usize, m_g: usize}
    let mut edges_g: HashSet<(usize, usize)> = HashSet::new();
    let mut edges_h: HashSet<(usize, usize)> = HashSet::new();

    for _ in 0..m_g {
        input! {u:usize, v:usize}
        edges_g.insert((u - 1, v - 1));
        edges_g.insert((v - 1, u - 1));
    }

    input! {m_h: usize}
    for _ in 0..m_h {
        input! {u:usize, v:usize}
        edges_h.insert((u - 1, v - 1));
        edges_h.insert((v - 1, u - 1));
    }

    let mut a = vec![vec![0; n]; n];
    for i in 0..n {
        for j in i + 1..n {
            input! {b:usize}
            a[i][j] = b;
            a[j][i] = b;
        }
    }

    let mut p = (0..n).collect::<Vec<usize>>();
    let mut ans = 28000000; // 初期値は十分大きい値に設定

    loop {
        let mut sum = 0;
        for i in 0..n {
            for j in 0..i {
                let h_contains = edges_h.contains(&(i, j));
                let g_contains = edges_g.contains(&(p[i], p[j]));
                if h_contains != g_contains {
                    sum += a[i][j];
                }
            }
        }
        ans = ans.min(sum);

        if !p.next_permutation() {
            break;
        }
    }
    println!("{}", ans);
}

