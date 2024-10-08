use proconio::input;

fn main() {
    input! {s:String}

    let ans = if s.ends_with("san") { "Yes" } else { "No" };
    print!("{}", ans);
}
