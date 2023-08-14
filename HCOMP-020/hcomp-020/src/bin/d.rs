use proconio::{fastout, input, marker::*};
#[macro_export]
macro_rules! read_line {
    ($($xs: tt)*) => {
        let mut buf = String::new();
        std::io::stdin().read_line(&mut buf).unwrap();
        let mut iter = buf.split_whitespace();
        expand!(iter, $($xs)*);
    };
}

#[macro_export]
macro_rules! expand {
    ($iter: expr,) => {};
    ($iter: expr, mut $var: ident : $type: tt, $($xs: tt)*) => {
        let mut $var = value!($iter, $type);
        expand!($iter, $($xs)*);
    };
    ($iter: expr, $var: ident : $type: tt, $($xs: tt)*) => {
        let $var = value!($iter, $type);
        expand!($iter, $($xs)*);
    };
}

#[macro_export]
macro_rules! value {
    ($iter:expr, ($($type: tt),*)) => {
        ($(value!($iter, $type)),*)
    };
    ($iter: expr, [$type: tt; $len: expr]) => {
        (0..$len).map(|_| value!($iter, $type)).collect::<Vec<_>>()
    };
    ($iter: expr, Chars) => {
        value!($iter, String).unwrap().chars().collect::<Vec<_>>()
    };
    ($iter: expr, $type: ty) => {
        if let Some(v) = $iter.next() {
            v.parse::<$type>().ok()
        } else {
            None
        }
    };
}

fn main() {
    read_line!(n: usize,);
    let n = n.unwrap();

    let mut ok = 0;
    let mut ng = n;

    while ng - ok > 1 {
        let mid = (ok + ng) / 2;

        println!("? {}", mid + 1);
        read_line!(x: usize,);
        let x = x.unwrap();

        if x == 0 {
            ok = mid;
        } else {
            ng = mid;
        }
    }

    println!("! {}", ok + 1);
}
