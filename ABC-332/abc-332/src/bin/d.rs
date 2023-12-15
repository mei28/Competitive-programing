use proconio::input;

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

fn get_inv(mut v: Vec<usize>) -> usize {
    let mut sum = 0;
    for i in 0..v.len() {
        for j in i + 1..v.len() {
            if v[i] > v[j] {
                v.swap(i, j);
                sum += 1;
            }
        }
    }
    sum
}

fn main() {
    input! {
        h: usize, w: usize,
        mut a: [[usize; w]; h],
        b: [[usize; w]; h],
    }

    let mut ans = vec![];

    let mut ph = (0..h).collect::<Vec<_>>();
    let mut pw = (0..w).collect::<Vec<_>>();

    for _ in 0..(1..=h).product() {
        for _ in 0..(1..=w).product() {
            let a = a.clone();
            let mut c = vec![vec![0; w]; h];
            for i in 0..h {
                for j in 0..w {
                    c[i][j] = a[ph[i]][pw[j]];
                }
            }

            if c == b {
                ans.push(get_inv(ph.clone()) + get_inv(pw.clone()));
            }

            pw.next_permutation();
        }
        ph.next_permutation();
    }

    if let Some(ans) = ans.iter().min() {
        println!("{ans}");
    } else {
        println!("-1");
    }
}

