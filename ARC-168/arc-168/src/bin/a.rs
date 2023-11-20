use proconio::{fastout, input, marker::Chars};

pub trait Monoid {
    type S;
    fn op(a: &Self::S, b: &Self::S) -> Self::S;
    fn id() -> Self::S;
}

pub struct AddMonoid;

impl Monoid for AddMonoid {
    type S = usize;
    fn op(a: &Self::S, b: &Self::S) -> Self::S {
        *a + *b
    }
    fn id() -> Self::S {
        0
    }
}

/// Let $\\{a_{i}\\}_{i=1}^{N}$ be a sequence of type Monoid::S.
#[derive(Clone)]
pub struct SegmentTree<M>
where
    M: Monoid,
{
    len: usize,
    size: usize,
    data: Vec<M::S>,
}

impl<M> SegmentTree<M>
where
    M: Monoid,
    M::S: Clone,
{
    /// Creates a segment tree with $\\{a_{i}\\}_{i=1}^{N}$ inside.
    /// n: lenght of $\\{a_{i}\\}_{i=1}^{N}$ (i.e. N)
    pub fn new(n: usize) -> Self {
        let size = n.next_power_of_two();
        SegmentTree::<M> {
            len: n,
            size,
            data: vec![M::id(); 2 * size - 1],
        }
    }

    /// Returns lenght of $\\{a_{i}\\}_{i=1}^{N}$ (i.e. Return N)
    pub fn len(&self) -> usize {
        self.len
    }

    /// Sets x to $a_{idx}$.
    pub fn set(&mut self, mut idx: usize, x: M::S) {
        idx += self.size - 1;
        self.data[idx] = x;
    }

    /// Builds segment tree.
    pub fn build(&mut self) {
        for idx in (0..self.size - 1).rev() {
            self.data[idx] = M::op(&self.data[2 * idx + 1], &self.data[2 * idx + 2]);
        }
    }

    /// Updates $a_{idx}$ to x.
    pub fn update(&mut self, mut idx: usize, x: M::S) {
        idx += self.size - 1;
        self.data[idx] = x;
        while idx > 0 {
            idx = (idx - 1) / 2;
            self.data[idx] = M::op(&self.data[2 * idx + 1], &self.data[2 * idx + 2]);
        }
    }

    /// Returns $a_{idx}$.
    pub fn get(&self, mut idx: usize) -> M::S {
        idx += self.size - 1;
        self.data[idx].clone()
    }

    /// Returns the result (fold op $\left[a_{l}, ... ,a_{r}\right)).$
    /// (i.e. Return $a_{l} (op) a_{l + 1} (op) \cdots (op) a_{r-1})$
    /// Notice that this is a half-opened section.
    pub fn fold(&self, mut l: usize, mut r: usize) -> M::S {
        l += self.size - 1;
        r += self.size - 1;

        let mut sum_l = M::id();
        let mut sum_r = M::id();

        while l < r {
            if l % 2 == 0 {
                sum_l = M::op(&sum_l, &self.data[l]);
            }
            if r % 2 == 0 {
                sum_r = M::op(&self.data[r - 1], &sum_r);
            }
            l = l / 2;
            r = (r - 1) / 2;
        }

        M::op(&sum_l, &sum_r)
    }
}

pub trait BinarySearch<T> {
    fn lower_bound(&self, key: &T) -> usize;
    fn upper_bound(&self, key: &T) -> usize;
}

impl<T> BinarySearch<T> for [T]
where
    T: Ord,
{
    fn lower_bound(&self, key: &T) -> usize {
        let mut ng = -1_isize;
        let mut ok = self.len() as isize;
        while ok - ng > 1 {
            let mid = (ok + ng) / 2;
            if *key <= self[mid as usize] {
                ok = mid;
            } else {
                ng = mid;
            }
        }
        ok as usize
    }

    fn upper_bound(&self, key: &T) -> usize {
        let mut ng = -1_isize;
        let mut ok = self.len() as isize;
        while ok - ng > 1 {
            let mid = (ok + ng) / 2;
            if *key < self[mid as usize] {
                ok = mid;
            } else {
                ng = mid;
            }
        }
        ok as usize
    }
}

pub fn compress<T>(v: &[T]) -> (Vec<usize>, Vec<T>)
where
    T: Ord + Clone,
{
    let mut scale = v.to_vec();
    scale.sort();
    scale.dedup();

    let mut cordinate = vec![];
    for a in v {
        cordinate.push(scale.lower_bound(a));
    }

    (cordinate, scale)
}

pub fn get_inversion_number(v: &[isize]) -> usize {
    let v = compress(v).0;
    let mut segtree = SegmentTree::<AddMonoid>::new(v.len());
    let mut ans = 0;
    for &x in v.iter() {
        ans += segtree.fold(x + 1, segtree.len());
        segtree.update(x, segtree.get(x) + 1);
    }

    ans
}

#[fastout]
fn main() {
    input! {
        n: usize,
        s: Chars,
    }

    let mut v = vec![];
    v.push(0);

    for i in 0..n - 1 {
        if s[i] == '<' {
            v.push(i as isize * 300000 + 1);
        } else {
            v.push(v[v.len() - 1] - 1);
        }
    }

    println!("{}", get_inversion_number(&v));
}

