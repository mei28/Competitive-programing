use proconio::input;

fn main() {
    input! {
        sx: u64, sy: u64,
        tx: u64, ty: u64,
    }

    let result = calculate_min_fee(sx, sy, tx, ty);
    println!("{}", result);
}

fn calculate_min_fee(sx: u64, sy: u64, tx: u64, ty: u64) -> u64 {
    // x座標の差
    let dx = if tx > sx { tx - sx } else { sx - tx };
    // y座標の差
    let dy = if ty > sy { ty - sy } else { sy - ty };

    // タイルの境界を通過する回数
    (dx + dy) / 2
}

