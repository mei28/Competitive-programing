use proconio::input;

fn main() {
    input! {n:usize, ps:[usize;n], qs:[usize;n]}

    let mut pq: Vec<_> = ps.iter().zip(qs.iter()).zip(1..=n).collect();
    pq.sort_by(|a, b| (a.1).cmp(b.1));

    for (a, b) in pq.iter() {
        let ans = pq[**a - 1].0;
        print!("{}", ans);
    }
}

