use proconio::{fastout, input, marker::Chars};

pub trait Permutation<T> {
    fn next_permutation(&mut self);
    fn prev_permutation(&mut self);
}

impl<T> Permutation<T> for [T]
where
    T: Ord,
{
    fn next_permutation(&mut self) {
        if self.len() <= 1 {
            return;
        }

        if let Some(i) = self.windows(2).rposition(|s| s[0] < s[1]) {
            let j = self.iter().rposition(|x| self[i] < *x).unwrap();
            self.swap(i, j);
            self[i + 1..].reverse();
        } else {
            self.reverse();
        }
    }

    fn prev_permutation(&mut self) {
        if self.len() <= 1 {
            return;
        }

        if let Some(i) = self.windows(2).rposition(|s| s[0] > s[1]) {
            let j = self.iter().rposition(|x| self[i] > *x).unwrap();
            self.swap(i, j);
            self[i + 1..].reverse();
        } else {
            self.reverse();
        }
    }
}

#[fastout]
fn main() {
    input! {
        n: usize, k: usize,
        s: Chars,
    }

    let mut set = vec![];

    let mut p = (0..n).collect::<Vec<_>>();
    loop {
        set.push(p.iter().cloned().map(|i| s[i]).collect::<Vec<_>>());
        p.next_permutation();
        if p == (0..n).collect::<Vec<_>>() {
            break;
        }
    }

    set.sort();
    set.dedup();

    let is_ok = |s: &Vec<char>| -> bool {
        for i in 0..n - k + 1 {
            let mut f = true;
            for j in 0..k {
                if s[i + j] != s[i + k - 1 - j] {
                    f = false;
                }
            }
            if f {
                return false;
            }
        }
        true
    };

    let ans = set.into_iter().filter(|s| is_ok(&s)).count();
    println!("{}", ans);
}

