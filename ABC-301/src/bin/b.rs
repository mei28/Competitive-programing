use proconio::input;

fn main() {
    input! {
        n: i32,
        a: [i32;n],
    }

    let mut ans = vec![];

    for i in 1..n {
        let left = a[(i - 1) as usize];
        let right = a[i as usize];
        let step;
        if left < right {
            step = 1;
            for i in (left..right).step_by(step) {
                ans.push(i);
            }
        } else {
            step = 1;
            for i in (right + 1..left + 1).step_by(step).rev() {
                ans.push(i);
            }
        }
    }
    ans.push(a[(n - 1) as usize]);
    println!(
        "{}",
        ans.iter()
            .map(|x| x.to_string())
            .collect::<Vec<_>>()
            .join(" ")
    );
}
