use proconio::{ fastout, input, marker::Chars };

#[fastout]
fn main() {
    input! {s:Chars,t:Chars}

    let mut j = 0;
    for i in 0..s.len() {
        let c = s[i];

        while j < t.len() {
            if c == t[j] {
                print!("{} ", j + 1);
                j += 1;
                break;
            }
            j += 1;
        }
    }
}
