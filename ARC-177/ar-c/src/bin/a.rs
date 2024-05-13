use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        mut a:usize,
        mut b:usize,
        mut c:usize,
        mut d:usize,
        mut e:usize,
        mut f:usize,
        n:usize,
        mut xs: [usize;n],
    }

    for mut x in xs {
        while x >= 500 && f >= 1 {
            x -= 500;
            f -= 1;
        }
        while x >= 100 && e >= 1 {
            x -= 100;
            e -= 1;
        }
        while x >= 50 && d >= 1 {
            x -= 50;
            d -= 1;
        }
        while x >= 10 && c >= 1 {
            x -= 10;
            c -= 1;
        }
        while x >= 5 && b >= 1 {
            x -= 5;
            b -= 1;
        }
        while x >= 1 && a >= 1 {
            x -= 1;
            a -= 1;
        }

        if x != 0 {
            println!("No");
            return;
        }
    }

    println!("Yes");
}
