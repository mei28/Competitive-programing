use proconio::input;

fn main() {
    input! {
        n: usize,
        events: [(usize, usize); n],
    }

    let mut water_amount = 0;
    let mut current_time = 0;

    for &(t_i, v_i) in &events {
        while current_time < t_i {
            if water_amount > 0 {
                water_amount -= 1;
            }
            current_time += 1;
        }

        water_amount += v_i;
    }

    println!("{}", water_amount);
}
