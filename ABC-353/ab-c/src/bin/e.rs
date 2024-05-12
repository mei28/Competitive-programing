use proconio::input;
fn main() {
    input! {
        n:usize,
        mut ss: [String;n]
    }
    ss.sort();
    ss.push(String::new());
    let mut stack = Vec::new();

    let mut ans = 0;

    for (i, s) in ss.iter().enumerate() {
        let lcp = stack
            .iter()
            .zip(s.chars())
            .take_while(|&(&(c, _), d)| c == d)
            .count();
        while stack.len() > lcp {
            let (_, start) = stack.pop().unwrap();
            ans += (i - start) * (i - start - 1) / 2;
        }

        for c in s[lcp..].chars() {
            stack.push((c, i));
        }
    }
    println!("{}", ans);
}
