use proconio::{fastout, input, marker::Chars};

fn rle(v: &Vec<char>) -> Vec<(char, usize)> {
    let n = v.len();
    let mut ans = vec![];

    let mut l = 0;
    while l < n {
        let mut r = l + 1;
        while r < n && v[l] == v[r] {
            r += 1;
        }
        ans.push((v[l], r - l));
        l = r;
    }
    ans
}

#[fastout]
fn main() {
    input! {n:usize,m:usize,s:Chars}
    let ret = rle(&s);
    let ans = ret.iter().map(|&x| x.1).max().unwrap();
    if ans == 1 {
        println!("{}", 0);
    } else {
        println!("{}", ans);
    }
}
