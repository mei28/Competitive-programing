use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {n:usize,m:usize,ss:[Chars;n]}
    let mut ans = n;

    for bits in 0..1 << n {
        let mut flg = vec![false; m];
        let mut cnt = 0;
        for i in 0..n {
            if bits >> i & 1 == 1 {
                cnt += 1;
                for j in 0..m {
                    if ss[i][j] == 'o' {
                        flg[j] = true;
                    }
                }
            }
        }

        if flg.iter().all(|&f| f) {
            ans = ans.min(cnt);
        }
    }
    println!("{}", ans);
}
