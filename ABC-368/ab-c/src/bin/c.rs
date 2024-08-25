use proconio::input;

fn main() {
    input! {n:usize,hs:[usize;n]}

    let mut t = 0;

    for mut a in hs {
        let num = a / 5;
        t += num * 3;
        a -= num * 5;
        while a > 0 {
            t += 1;
            if t % 3 == 0 {
                a -= 3;
            } else {
                a -= 1;
            }
        }
    }
    println!("{}", t);
}
