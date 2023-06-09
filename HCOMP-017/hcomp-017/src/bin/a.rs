use proconio::{fastout, input};

fn gcd(mut a: usize, mut b: usize) -> usize {
    while b != 0 {
        let tmp = a;
        a = b;
        b = tmp % a;
    }
    return a;
}

#[fastout]
fn main() {
    input! {n:usize,x:usize,xs : [usize;n]}
    let mut ds = vec![];
    for i in 0..n {
        ds.push((xs[i] as isize - x as isize).abs() as usize);
    }

    let mut ans = ds[0];
    for d in ds.iter() {
        ans = gcd(ans, *d);
    }
    println!("{}", ans)
}
