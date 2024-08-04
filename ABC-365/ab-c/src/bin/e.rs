use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }

    let mut xor_accum = vec![0; n + 1];
    for i in 0..n {
        xor_accum[i + 1] = xor_accum[i] ^ a[i];
    }

    let mut total_sum = 0;

    for i in 0..n {
        for j in (i + 1)..n {
            total_sum += xor_accum[j + 1] ^ xor_accum[i];
        }
    }

    println!("{}", total_sum);
}
