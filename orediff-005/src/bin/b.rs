use proconio::{fastout, input};
use std::collections::BTreeSet;

#[fastout]
fn main() {
    input! {
        n: usize,
        k: usize,
        ps: [usize; n],
    }

    let mut under = vec![-1; n + 5];
    let mut pile = vec![0; n + 5];
    let mut st = BTreeSet::new();
    let mut res = vec![-1; n + 5];

    for i in 0..n {
        let p = ps[i];
        let mut it = st.range(p + 1..).next().cloned();

        match it {
            Some(val) => {
                under[p] = val as i32;
                pile[p] = pile[val] + 1;
                st.remove(&val);
            }
            None => {
                pile[p] = 1;
            }
        }
        st.insert(p);

        if pile[p] == k as i32 {
            st.remove(&p);
            let mut x = p;
            for _ in 0..k {
                res[x] = i as i32 + 1; // 1-indexed output
                x = under[x] as usize;
            }
        }
    }

    for i in 1..=n {
        println!("{}", res[i]);
    }
}
