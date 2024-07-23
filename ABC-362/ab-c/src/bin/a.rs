use proconio::input;
fn main() {
    input! {r:usize,g:usize,b:usize ,s: String}
    let ans = {
        match s.as_str() {
            "Red" => g.min(b),
            "Green" => r.min(b),
            "Blue" => r.min(g),
            _ => unreachable!(),
        }
    };
    println!("{}", ans);
}
