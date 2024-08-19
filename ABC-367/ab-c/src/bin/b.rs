use proconio::input;

fn main() {
    input! {
        x: f64
    }

    println!(
        "{}",
        format!("{:.3}", x)
            .trim_end_matches('0')
            .trim_end_matches('.')
    );
}
