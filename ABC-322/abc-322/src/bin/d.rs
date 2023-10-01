use itertools::{iproduct, Itertools};
use proconio::{fastout, input, marker::Chars};

#[fastout]
fn main() {
    input! { p: [[Chars;4];3] }

    let mut sum = 0;
    for i in 0..3 {
        for j in 0..4 {
            for k in 0..4 {
                if p[i][j][k] == '#' {
                    sum += 1;
                }
            }
        }
    }
    if sum < 16 {
        println!("No");
        return;
    }

    for (r1, r2) in iproduct!(0..4, 0..4) {
        for (i1, j1, i2, j2, i3, j3) in iproduct!(0..7, 0..7, 0..7, 0..7, 0..7, 0..7) {
            let mut p1 = p[0].clone();
            for _ in 0..r1 {
                rotate(&mut p1);
            }
            let mut p2 = p[1].clone();
            for _ in 0..r2 {
                rotate(&mut p2);
            }
            let p3 = p[2].clone();

            if solve(&p1, &p2, &p3, i1, j1, i2, j2, i3, j3) == sum {
                println!("Yes");
                return;
            }
        }
    }
    println!("No");
}
fn rotate(b: &mut Vec<Vec<char>>) {
    let mut res = vec![vec!['.'; 4]; 4];
    for i in 0..4 {
        for j in 0..4 {
            res[i][j] = b[j][3 - i];
        }
    }
    *b = res;
}

fn solve(
    p1: &Vec<Vec<char>>,
    p2: &Vec<Vec<char>>,
    p3: &Vec<Vec<char>>,
    i1: usize,
    j1: usize,
    i2: usize,
    j2: usize,
    i3: usize,
    j3: usize,
) -> usize {
    let mut b = vec![vec!['.'; 4]; 4];
    for i in 0..4 {
        for j in 0..4 {
            if i + 3 >= i1
                && i + 3 - i1 < 4
                && j + 3 >= j1
                && j + 3 - j1 < 4
                && p1[i + 3 - i1][j + 3 - j1] == '#'
            {
                b[i][j] = '#';
            }
            if i + 3 >= i2
                && i + 3 - i2 < 4
                && j + 3 >= j2
                && j + 3 - j2 < 4
                && p2[i + 3 - i2][j + 3 - j2] == '#'
            {
                b[i][j] = '#';
            }
            if i + 3 >= i3
                && i + 3 - i3 < 4
                && j + 3 >= j3
                && j + 3 - j3 < 4
                && p3[i + 3 - i3][j + 3 - j3] == '#'
            {
                b[i][j] = '#';
            }
        }
    }

    let mut temp = 0;
    for (i, j) in iproduct!(0..4, 0..4) {
        if b[i][j] == '#' {
            temp += 1;
        }
    }
    temp
}
