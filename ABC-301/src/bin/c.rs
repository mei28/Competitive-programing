use proconio::input;
use proconio::marker::Chars;

const AT: [char; 7] = ['a', 't', 'c', 'o', 'd', 'e', 'r'];

fn main() {
    input! {
        s: Chars,
        t: Chars,
    }

    let mut dct_s = vec![0; 26];
    let mut dct_t = vec![0; 26];
    let mut cnt_s = 0;
    let mut cnt_t = 0;

    for i in 0..s.len() {
        if s[i] == '@' {
            cnt_s += 1;
        } else {
            dct_s[s[i] as usize - 'a' as usize] += 1;
        }
    }

    for i in 0..t.len() {
        if t[i] == '@' {
            cnt_t += 1;
        } else {
            dct_t[t[i] as usize - 'a' as usize] += 1;
        }
    }

    let mut ok: bool = true;

    for i in 0..26 {
        if dct_s[i] == dct_t[i] {
            continue;
        }

        let c = std::char::from_u32((i + 'a' as usize) as u32).unwrap();
        if !AT.iter().any(|x| *x == c) {
            ok = false;
            break;
        }
        if dct_s[i] > dct_t[i] {
            cnt_t -= dct_s[i] - dct_t[i];
            if cnt_t < 0 {
                ok = false;
                break;
            }
        } else {
            cnt_s -= dct_t[i] - dct_s[i];
            if cnt_s < 0 {
                ok = false;
                break;
            }
        }
    }

    println!("{}", if ok { "Yes" } else { "No" });
}
