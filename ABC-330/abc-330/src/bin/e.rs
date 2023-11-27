use proconio::input;
use std::collections::BTreeSet;

fn main() {
    input! {
        n: usize,
        mut q: usize,
        mut a: [usize; n],
    }

    let mut bk = vec![0; n + 1];
    for i in 0..n {
        if a[i] <= n {
            bk[a[i]] += 1;
        }
    }

    let mut st = BTreeSet::new();
    for i in 0..=n {
        if bk[i] == 0 {
            st.insert(i);
        }
    }

    while q > 0 {
        q -= 1;
        input! {
            i_input: usize,
            x: usize
        }
        let i = i_input - 1; // Adjust the index to be 0-based

        if a[i] <= n {
            bk[a[i]] -= 1;
            if bk[a[i]] == 0 {
                st.insert(a[i]);
            }
        }

        a[i] = x;
        if a[i] <= n {
            if bk[a[i]] == 0 {
                st.remove(&a[i]);
            }
            bk[a[i]] += 1;
        }
        println!("{}", st.iter().next().unwrap_or(&0));
    }
}

