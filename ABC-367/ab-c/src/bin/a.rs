use proconio::input;

fn main() {
    input! {a:usize, b:usize,c:usize}

    let mut i = a;

    while i != b {
        if i == c {
            println!("No");
            return;
        }
        i += 1;
        i %= 24;
    }
    println!("Yes");
}
