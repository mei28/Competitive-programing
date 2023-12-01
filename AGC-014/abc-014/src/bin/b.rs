use proconio::{fastout, input, marker::Usize1};

#[fastout]
fn main() {
    input! {n:usize,m:usize,qs : [(Usize1,Usize1);m]}

    let mut g = vec![0; n];
    for (a, b) in qs {
        g[a] += 1;
        g[b] += 1;
    }

    let ans = g.iter().all(|x| x % 2 == 0);
    println!("{}", if ans { "YES" } else { "NO" });
}
