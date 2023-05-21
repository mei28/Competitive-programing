use cmp::{max, min, Reverse};
use itertools::Itertools;
use proconio::{fastout, input, marker::*};
use std::collections::*;
use std::*;

#[fastout]
fn main() {
    input! {
        n: usize,
        m: usize,
        s: [String; n],
    }

    for perm in (0..n).permutations(n) {
        let mut tmp = vec![];
        for i in perm {
            tmp.push(s[i].clone());
        }
        let mut flg = true;

        for j in 1..n {
            let left = &tmp[j - 1];
            let right = &tmp[j];
            let mut cnt = 0;

            for i in 0..m {
                if left.chars().nth(i) != right.chars().nth(i) {
                    cnt += 1;
                }
            }

            if cnt > 1 {
                flg = false;
            }
        }

        if flg {
            println!("Yes");
            return;
        }
    }
    println!("No");
}
