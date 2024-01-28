use proconio::{input, marker::Usize1};
use std::mem::swap;

fn main() {
    input! {
        n: usize,
    }
    let mut ab = vec![];
    let mut v: Vec<(usize, usize)> = vec![(0, 0); 2 * n + 10];

    for i in 0..n {
        input! {
            mut a: Usize1,
            mut b: Usize1,
        }
        if a > b {
            swap(&mut a, &mut b);
        }

        ab.push((a, b));
        v[a] = (0, i);
        v[b] = (1, i);
    }

    let mut st = vec![];

    for i in 0..2 * n {
        let (t, id) = v[i];
        if t == 0 {
            st.push(id);
        } else {
            if *st.last().unwrap() != id {
                println!("Yes");
                return;
            }
            st.pop();
        }
    }

    println!("No");
}
