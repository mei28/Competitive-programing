use proconio::input;

fn get_totalarea(r: usize, A: &Vec<usize>) -> usize {
    let mut area = 0;
    for &a in A.iter() {
        if a >= r {
            area += (1 << a) * (1 << a);
        }
    }
    area
}

fn main() {
    input! {
        h: usize,
        w: usize,
        n: usize,
        aa: [usize; n],
    }

    for r in 0..=25 {
        let limit_h = h / (1 << r);
        let limit_w = w / (1 << r);
        let limit_area = limit_h * limit_w * (1 << r) * (1 << r);

        let actual_area = get_totalarea(r, &aa);

        if actual_area > limit_area {
            println!("No");
            return;
        }
    }
    println!("Yes");
}
