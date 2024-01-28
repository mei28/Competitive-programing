use proconio::{fastout, input, marker::Usize1};

fn dist(from: usize, to: usize, n: usize) -> usize {
    if from <= to {
        to - from
    } else {
        to + n - from
    }
}

fn add(from: usize, to: usize, num: usize, n: usize, v: &mut Vec<usize>) {
    if from <= to {
        v[from] += num;
        v[to] -= num;
    } else {
        v[from] += num;
        v[n] -= num;
        v[0] += num;
        v[to] -= num;
    }
}

#[fastout]
fn main() {
    input! {n:usize,m:usize,x:[Usize1;m]}
    let mut v = vec![0; n + 1];

    let mut ans = std::usize::MAX;

    for i in 0..m - 1 {
        add(x[i], x[i + 1], dist(x[i + 1], x[i], n), n, &mut v);
        add(x[i + 1], x[i], dist(x[i], x[i + 1], n), n, &mut v);
    }

    for i in 0..n {
        v[i + 1] += v[i];
        ans = std::cmp::min(ans, v[i]);
    }
    println!("{}", ans);
}

