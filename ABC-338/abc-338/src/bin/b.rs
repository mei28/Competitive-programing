use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! {s:Chars}
    let mut cnt = vec![0; 128];
    let mut m_cnt = 0;

    for c in s {
        let idx = (c as u8 - 'a' as u8) as usize;
        cnt[idx] += 1;
        m_cnt = m_cnt.max(cnt[idx]);
    }

    for i in 0..128 {
        if cnt[i] == m_cnt {
            println!("{}", (i as u8 + 'a' as u8) as char);
            return;
        }
    }
}
