use proconio::input;

pub trait BinarySearch<T> {
    fn lower_bound(&self, key: T) -> usize;
}

impl<T> BinarySearch<T> for [T]
where
    T: Ord,
{
    fn lower_bound(&self, key: T) -> usize {
        let mut ng = -1_isize;
        let mut ok = self.len() as isize;
        while ok - ng > 1 {
            let mid = (ok + ng) / 2;
            if self[mid as usize] >= key {
                ok = mid;
            } else {
                ng = mid;
            }
        }
        ok as usize
    }
}

fn main() {
    input! {
        n: usize,
        m: usize,
        mut a: [usize; n],
        mut b: [usize; m],
    }

    let mut people: Vec<(usize, usize)> = a.iter().enumerate().map(|(i, &x)| (x, i + 1)).collect();
    people.sort_by_key(|&(x, _)| x);

    let mut sushi: Vec<(usize, usize)> = b.iter().enumerate().map(|(i, &x)| (x, i)).collect();
    sushi.sort_by_key(|&(x, _)| x);

    let mut result = vec![-1; m];

    let mut person_idx = 0;

    for (bi, orig_idx) in sushi {
        while person_idx < n && people[person_idx].0 < bi {
            person_idx += 1;
        }

        if person_idx < n {
            result[orig_idx] = people[person_idx].1 as i32;
        }
    }

    for res in result {
        println!("{}", res);
    }
}
