use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {h: isize, w: isize, n: usize}

    let dx: [isize; 4] = [0, 1, 0, -1];
    let dy: [isize; 4] = [-1, 0, 1, 0];
    let mut idx: isize = 0; // 初期方向は上
    let mut map = vec![vec!['.'; w as usize]; h as usize]; // 全てのマスを白（'.'）で初期化
    let mut now: (isize, isize) = (0, 0); // (1, 1) は0始まりで (0, 0)

    for _ in 0..n {
        if map[now.0 as usize][now.1 as usize] == '.' {
            map[now.0 as usize][now.1 as usize] = '#'; // 白のマスを黒に塗り替える
            idx = (idx + 1) % 4; // 時計回りに90度回転
        } else {
            map[now.0 as usize][now.1 as usize] = '.'; // 黒のマスを白に塗り替える
            idx = (idx - 1 + 4) % 4; // 反時計回りに90度回転
        }
        now = (
            (now.0 + dy[idx as usize] + h) % h,
            (now.1 + dx[idx as usize] + w) % w,
        ); // トーラス状のグリッドを考慮
    }

    for row in map.iter() {
        let line: String = row.iter().collect();
        println!("{}", line);
    }
}

