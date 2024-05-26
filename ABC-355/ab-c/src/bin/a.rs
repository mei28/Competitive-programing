use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {a:usize,b:usize}
    if a==b{println!("-1");return;}

    for i in 1..=3{
        if i!= a && i!=b{
            println!("{}",i);
            return;
        }
    }
}
