use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        a:isize,
        b:isize,
        c:isize,
        d:isize,
        e:isize,
        f:isize,
        g:isize,
        h:isize,
        i:isize,
        j:isize,
        k:isize,
        l:isize,
    }

    let flg = {
        let ag = a.max(g);
        let dj = d.min(j);
        let bh = b.max(h);
        let ek = e.min(k);
        let ci = c.max(i);
        let fl = f.min(l);

        if ag < dj && bh < ek && ci < fl {
            true
        } else {
            false
        }
    };
    println!("{}", if flg { "Yes" } else { "No" });
}
