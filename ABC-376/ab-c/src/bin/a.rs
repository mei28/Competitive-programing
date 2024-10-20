use proconio::input;

fn main() {
    input! {n:usize,c:usize,ts: [usize;n]}

    let mut ans = 1;
    let mut now = ts[0];

    for i in 1..n {
        if now <= ts[i] {
            ans += 1;
            now = ts[i];
        }
        now += c;
    }
    println!("{}", ans);
}
