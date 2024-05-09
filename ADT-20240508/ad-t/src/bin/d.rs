use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        ss: [Chars; n],
    }

    let ans = (0..n)
        .flat_map(|i| {
            (i + 1..n).filter_map(|j| {
                (0..m)
                    .all(|k| ss[i][k] == 'o' || ss[j][k] == 'o')
                    .then(|| 1)
            })
        })
        .sum::<usize>();

    println!("{}", ans);
}

