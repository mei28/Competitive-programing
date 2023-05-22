use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,q:usize}

    let mut head = vec![-1; n + 1];
    let mut tail = vec![-1; n + 1];

    for _ in 0..q {
        input! {t:usize}
        if t == 1 {
            input! {x:usize, y:usize}
            tail[x] = y as isize;
            head[y] = x as isize;
        }
        if t == 2 {
            input! {x:usize, y:usize}
            tail[x] = -1;
            head[y] = -1;
        }
        if t == 3 {
            input! {mut x:isize}
            while head[x as usize] != -1 {
                x = head[x as usize];
            }

            let mut ans = vec![];
            while x != -1 {
                ans.push(x);
                x = tail[x as usize];
            }

            let ans: Vec<String> = ans.into_iter().map(|x| x.to_string()).collect();
            println!("{} {}", ans.len(), ans.join(" "));
        }
    }
}
