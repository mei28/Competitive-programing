use proconio::input;

fn main() {
    input! {
        n: usize,
        x: usize,
        y: usize,
        aa: [usize; n],
        bb: [usize; n],
    }

    let mut ab = aa.iter().zip(bb.iter()).collect::<Vec<_>>();

    ab.sort_by(|a, b| b.0.cmp(a.0));

    let mut mut_x = 0;
    let mut mut_y = 0;
    let mut i_a = n - 1;
    for (i, &(a, b)) in ab.iter().enumerate() {
        mut_x += a;
        mut_y += b;
        if mut_x > x || mut_y > y {
            i_a = i;
            break;
        }
    }

    ab.sort_by(|a, b| b.1.cmp(a.1));

    let mut mut_x2 = 0;
    let mut mut_y2 = 0;
    let mut i_b = n - 1;
    for (i, &(a, b)) in ab.iter().enumerate() {
        mut_x2 += a;
        mut_y2 += b;
        if mut_x2 > x || mut_y2 > y {
            i_b = i;
            break;
        }
    }

    println!("{}", i_a.min(i_b) + 1);
}
