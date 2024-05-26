use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {n:usize,m:usize,aa:[usize;n],bb:[usize;m]}

    let mut v: Vec<(usize, char)> = vec![];

    for a in aa {
        v.push((a, 'a'));
    }
    for b in bb {
        v.push((b, 'b'));
    }

    v.sort_by(|a, b| a.0.cmp(&b.0));

    for i in 1..(n+m){
        if v[i].1=='a' && v[i-1].1=='a'{
            println!("Yes");
            return;
        }
    }
    println!("No");
}
