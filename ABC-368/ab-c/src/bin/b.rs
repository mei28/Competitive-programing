use proconio::input;

fn main() {
    input! {n:usize,mut aa:[usize;n] }

    let mut cnt = 0;

    aa.sort();

    loop {
        aa.sort();
        if aa[n - 2] == 0 || aa[n - 1] == 0 {
            break;
        }

        aa[n - 2] -= 1;
        aa[n - 1] -= 1;
        cnt += 1;
    }
    println!("{}", cnt);
}
