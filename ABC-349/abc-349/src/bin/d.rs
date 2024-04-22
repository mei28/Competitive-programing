use proconio::input;

fn main() {
    input! {
        mut l: usize,
        mut r: usize,
    }

    let mut left = Vec::new();
    let mut right = Vec::new();

    let mut p = 0;

    while l < r {
        if l % 2 == 1 {
            left.push((l << p, (l + 1) << p));
            l += 1;
        }
        if r % 2 == 1 {
            r -= 1;
            right.push((r << p, (r + 1) << p));
        }
        l >>= 1;
        r >>= 1;
        p += 1;
    }

    let ans = left
        .iter()
        .chain(right.iter().rev())
        .copied()
        .collect::<Vec<_>>();

    println!("{}", ans.len());
    for (l, r) in ans {
        println!("{} {}", l, r);
    }
}
